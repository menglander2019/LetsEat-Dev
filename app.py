from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from backend.db.db_management import *
from backend.questions_data import *
from restaurant_suggester import get_predictions
import os

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

user_middlewares = []
user_middlewares.append(Middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]))
user_middlewares.append(Middleware(SessionMiddleware, secret_key=os.environ.get('secret_key')))

app = FastAPI(middleware=user_middlewares)

@app.post("/checkLogin")
async def checkLogin(request: Request):
    login_data = await request.json()
    email = login_data["data"][0]["selectedChoices"][0]
    password = login_data["data"][1]["selectedChoices"][0]
    print(email)
    print(password)
    # returns the user's ID if it exists and a TRUE/FALSE value (1/0)
    response = checkUser(email, password)
    token = ""
    print(response)
    if response[0] == 1:
        request.session["id"] = response[1]
        token = "fjdsfkjasdflkjsl"
    return {
        "status": response[0],
        "token": token
    }

@app.post("/logout")
async def logout(request: Request):
    request.session.clear()
    return {"status": "cleared"}

@app.post("/testCheckLogin")
def testCheckLogin():
    return [ 
        {
            "status": 0,
            "token": None
        }
    ]

@app.post("/checkLoginPositive")
async def testCheckLoginPositive(request: Request):
    account_data = await request.json()
    return {
        "status": 1,
        "token": "#kdudhn23232nds@3"
    }

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
    updatePositives("test@test.com", "italian")
    updateNegatives("test@test.com", "chinese")
    updateRestrictions("test@test.com", "vegetarian")
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
    #suggestions_list = get_predictions(id, occasion, num_people, meal, price_ranges)
    #return {"message": suggestions_list}
    return {"message": "temp"}

@app.get("/isNewUser")
async def is_new_user(request: Request):
    id = request.session["id"]
    print(id)
    res = checkNewUser(id)
    return {"status": res} # 1 is new user, 0 is existing

@app.get("/getRecommendations")
def getRecommendations():
    return {"message": "recommendation"}
