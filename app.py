from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from backend.db.db_management import *
from backend.questions_data import *
from restaurant_suggester import get_predictions, get_group_predictions
from yelp.YelpApiCalls import return_business
from backend.group_session import *
import os
import jwt

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

user_middlewares = []
user_middlewares.append(Middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]))
#user_middlewares.append(Middleware(SessionMiddleware, secret_key='test_secret'))
user_middlewares.append(Middleware(SessionMiddleware, secret_key=os.environ.get('secret_key')))

app = FastAPI(middleware=user_middlewares)

groupHost_dict = {}

@app.post("/checkLogin")
async def checkLogin(request: Request):
    login_data = await request.json()
    email = login_data["data"][0]["selectedChoices"][0]
    password = login_data["data"][1]["selectedChoices"][0]
    # returns the user's ID if it exists and a TRUE/FALSE value (1/0)
    response = checkUser(email, password)
    token = ""
    # if the response is 1 (meaning a valid user login), then set up the session data and return a token
    if response[0] == 1:
        request.session["id"] = response[1]
        token = jwt.encode(login_data, "secret", algorithm="HS256")
    return {
        "status": response[0],
        "token": token
    }

@app.post("/logout")
async def logout(request: Request):
    request.session.clear()
    return {"status": "cleared"}

@app.post("/createprofile")
async def createprofile(request: Request):
    account_data = await request.json()
    email = account_data["data"][0]["selectedChoices"][0]
    password = account_data["data"][1]["selectedChoices"][0]
    name = account_data["data"][2]["selectedChoices"][0]
    dob = account_data["data"][3]["selectedChoices"][0]
    gender = account_data["data"][4]["selectedChoices"][0]
    createUser(email, password, name, dob, gender)
    return {"message": "Profile created!"}

@app.get("/questionnaire/login/")
def questionnaire_login():
    return {"data": login_questions}

@app.get("/questionnaire/profile/")
def questionnaire_profile():
    return {"data": profile_questions}

@app.get("/questionnaire/createprofile/")
def questionnaire_createProfile():
    return {"data": createprofile_questions}

@app.get("/questionnaire/search/")
def questionnaire_search():
    return {"data": search_questions}

@app.post("/submit/profile/")
async def submit_questionnaire(request: Request):
    profile_data = await request.json()
    # extracts the positives, restrictions, and negatives from the JSON sent from REACT and checks for any None objects
    positives = profile_data["data"][0]["selectedChoices"]
    if None in positives:
        print("WARNING! Found a None object in positives passed from REACT. Removing...")
        positives.remove(None)

    restrictions = profile_data["data"][1]["selectedChoices"]
    if None in restrictions:
        print("WARNING! Found a None object in restrictions passed from REACT. Removing...")
        restrictions.remove(None)

    negatives = profile_data["data"][2]["selectedChoices"]
    if None in negatives:
        print("WARNING! Found a None object in negatives passed from REACT. Removing...")
        negatives.remove(None)

    id = request.session["id"]
    # convert the tuples of positives, restrictions, and negatives into lists in their proper formats
    positives_list = []
    negatives_list = []
    restrictions_list = []
    for positive in positives:
        if positive not in cuisine_groups:
            raise Exception("ERROR: Positive value (" + str(positive) + ") gotten from REACT app does not match cuisine groups!")
        positives_list.append(cuisine_groups[positive])
    for negative in negatives:
        if negative not in cuisine_groups:
            raise Exception("ERROR: Negative value (" + str(negative) + ") gotten from REACT app does not match cuisine groups!")
        negatives_list.append(cuisine_groups[negative])
    for restriction in restrictions:
        if restriction not in restrictions_dict:
            raise Exception("ERROR: Value (" + str(restriction) + ") gotten from REACT app does not match restriction groups!")
        restrictions_list.append(restrictions_dict[restriction])
    updatePositives(id, positives_list)
    updateNegatives(id, negatives_list)
    # checks if the N/A option is selected
    if len(restrictions) != 1 or restrictions[0] != 'N/A':
        updateRestrictions(id, restrictions_list)
    return {"message": "submitted"}

@app.post("/submit/search/")
async def submit_search(request: Request):
    search_data = await request.json()
    # extracts all the search criteria from the selected answers
    id = request.session["id"]
    occasion = search_data["data"][0]["selectedChoices"][0]
    num_people = int(search_data["data"][1]["selectedChoices"][0])
    meal = search_data["data"][2]["selectedChoices"][0]
    price_ranges = search_data["data"][3]["selectedChoices"]
    zip = search_data["data"][4]["selectedChoices"][0]
    # converts the $$$'s selected into numbers
    actual_price_ranges = []
    for price in price_ranges:
        actual_price_ranges.append(price_ranges_groups[price])
    suggestions_list = get_predictions(id, occasion, num_people, meal, actual_price_ranges, zip)
    request.session.update({"rest_id_list": suggestions_list})
    return {"message": "submitted"}

@app.get("/isNewUser/")
async def is_new_user(request: Request):
    id = request.session["id"]
    res = checkNewUser(id)
    return {"status": res} # 1 is new user, 0 is existing

@app.get("/getRecommendations/")
def getRecommendations(request: Request):
    rest_list = []
    if "rest_id_list" in request.session:
        for id in request.session['rest_id_list']:
            rest_list.append(return_business(id))
    return {"restaurants": rest_list}

@app.post("/createGroupSession")
def createGroupSession(request: Request):
    groupHost_dict[request.session["id"]] = []
    return {"message": "group session created"}

@app.post("/deleteGroupSession")
def deleteGroupSession(request: Request):
    hostID = request.session["id"]
    if hostID in groupHost_dict:
        del groupHost_dict[hostID]
        response = "deleted host ID: " + str(hostID)
    else:
        response = "host ID: " + str(hostID) + " not found!"
    return {"message": response}

@app.post("/joinGroup/{hostID}")
def joinGroupSession(hostID: int, request: Request):
    response = "group " + str(hostID) + " not found"
    if hostID in groupHost_dict:
        print("found host!")
        joiningID = request.session["id"]
        if joiningID in groupHost_dict[hostID]:
            response = "already joined group: " + str(hostID)
        else:
            groupHost_dict[hostID].append(joiningID)
            response = "group " + str(hostID) + " found and joined"
        print(groupHost_dict)

    return {"message": response}

@app.get("/getGroupRecommendations")
async def getGroupRecommendations(request: Request):
    group_search_data = await request.json()
    # retrieves group ID based on the host's ID
    hostID = request.session["id"]
    groupIDs = groupHost_dict[hostID]
    # generates the list of positives, negatives, and restrictions based on the group
    positives = generateGroupPreferences(hostID, groupIDs)
    negatives = generateGroupNegatives(hostID, groupIDs)
    restrictions = generateGroupRestrictions(hostID, groupIDs)

    # uses the request body to get the search preferences
    occasion = group_search_data["data"][0]["selectedChoices"][0]
    num_people = int(group_search_data["data"][1]["selectedChoices"][0])
    meal = group_search_data["data"][2]["selectedChoices"][0]
    price_ranges = group_search_data["data"][3]["selectedChoices"]
    zip = group_search_data["data"][4]["selectedChoices"][0]
    # converts the $$$'s selected into numbers
    actual_price_ranges = []
    for price in price_ranges:
        actual_price_ranges.append(price_ranges_groups[price])

    # uses a new group prediction function to generate the list of suggested restaurants
    group_suggestions_list = get_group_predictions(positives, negatives, restrictions, occasion, num_people, meal, actual_price_ranges, zip)

    # temporarily having the function return the list of restaurants, will eventually just populate the session with IDs
    # and a separate route will return the list of restaurants
    rest_list = []
    for id in group_suggestions_list:
        rest_list.append(return_business(id))
    return {"restaurants": rest_list}
