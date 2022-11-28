from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from backend.db.db_management import *
from backend.questions_data import *
from restaurant_suggester import get_predictions
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

@app.post("/checkLogin")
async def checkLogin(request: Request):
    print(request)
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
    # extracts the positives, restrictions, and negatives from the JSON sent from REACT
    positives = profile_data["data"][0]["selectedChoices"]
    restrictions = profile_data["data"][1]["selectedChoices"]
    negatives = profile_data["data"][2]["selectedChoices"]
    id = request.session["id"]
    # convert the tuples of positives, restrictions, and negatives into lists in their proper formats
    positives_list = []
    negatives_list = []
    restrictions_list = []
    for positive in positives:
        if positive not in cuisine_groups:
            raise Exception("ERROR: Value gotten from REACT app does not match cuisine groups!")
        positives_list.append(cuisine_groups[positive])
    for negative in negatives:
        if negative not in cuisine_groups:
            raise Exception("ERROR: Value gotten from REACT app does not match cuisine groups!")
        negatives_list.append(cuisine_groups[negative])
    for restriction in restrictions:
        if restriction not in restrictions_dict:
            raise Exception("ERROR: Value gotten from REACT app does not match cuisine groups!")
        restrictions_list.append(restrictions_dict[restriction])
    updatePositives(id, positives_list)
    updateNegatives(id, negatives_list)
    updateRestrictions(id, restrictions_list)
    return {"message": "submitted"}

@app.post("/submit/search/")
async def submit_search(request: Request):
    search_data = await request.json()
    # extracts all the search criteria from the selected answers
    id = request.session["id"]
    print(id)
    occasion = search_data["data"][0]["selectedChoices"]
    num_people = search_data["data"][1]["selectedChoices"]
    meal = search_data["data"][2]["selectedChoices"]
    price_ranges = search_data["data"][3]["selectedChoices"]
    distance_settings = search_data["data"][4]["selectedChoices"]
    suggestions_list = get_predictions(id, occasion, num_people, meal, price_ranges)
    request.session["rest_list"] = suggestions_list
    return {
        "status": 200
    }

@app.get("/isNewUser/")
async def is_new_user(request: Request):
    id = request.session["id"]
    res = checkNewUser(id)
    return {"status": res} # 1 is new user, 0 is existing

@app.get("/getRecommendations")
def getRecommendations(request: Request):
    return {"restaurants": request.session["rest_list"]}
