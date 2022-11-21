from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.db.db_management import *
from backend.questions_data import *
from .restaurant_suggester import get_predictions

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "home"}

@app.get("/checkLogin")
def checkLogin():
    return {"data": 0}

@app.get("/checkLoginPositive")
def checkLoginPositive():
    return {"data": 1}

@app.get("/about")
def about():
    return {"message": "about"}

@app.get("/login")
def login():
    return {"message": "login page"}

@app.get("/signup")
def signup():
    return {"message": "signup page"}

@app.post("/createprofile")
async def createprofile(request: Request):
    account_data = await request.json()
    #print(account_data["data"])
    email = account_data["data"][0]["selectedChoices"][0]
    password = account_data["data"][1]["selectedChoices"][0]
    name = account_data["data"][2]["selectedChoices"][0]
    dob = account_data["data"][3]["selectedChoices"][0]
    gender = account_data["data"][4]["selectedChoices"][0]
    createUser(email, password, name, dob, gender)
    return {"message": "account created"}

@app.get("/questionnaire/profile/")
def questionnaire_profile():
    return {"data": profile_questions}

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
    id = 1234 # placeholder, need to get ID here
    occasion = search_data["data"][0]["selectedChoices"]
    num_people = search_data["data"][1]["selectedChoices"]
    meal = search_data["data"][2]["selectedChoices"]
    price_ranges = search_data["data"][3]["selectedChoices"]
    distance_settings = search_data["data"][4]["selectedChoices"]
    suggestions_list = get_predictions(id, occasion, num_people, meal, price_ranges)
    return {"message": suggestions_list}

@app.get("/recommendation")
def recommendation():
    return {"message": "recommendation"}

