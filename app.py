from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.db.db_management import createUser
from backend.questions_data import *

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

@app.get("/about")
def about():
    return {"message": "about"}

@app.get("/login")
def login():
    return {"message": "login page"}

@app.get("/signup")
def signup():
    return {"message": "signup page"}

@app.post("/signup/email/{email}/pw/{pw}/name/{name}/dob/{dob}/gender/{gender}/pos/{pos}/neg/{neg}/restr/{restr}")
def signup(email, pw, name, dob, gender, pos, neg, restr):
    return createUser(email, pw, name, dob, gender, pos, neg, restr)

@app.get("/createprofile")
def createprofile():
    return {"message": "createprofile"}

@app.get("/questionnaire/profile/")
def questionnaire_profile():
    return {"data": profile_questions}

@app.get("/questionnaire/search/")
def questionnaire_search():
    return {"data": search_questions}

@app.post("/submit/profile/")
async def submit_questionnaire(request: Request):
    returnData = await request.json()
    return {"message": "submitted"}

@app.post("/submit/search/")
async def submit_search(request: Request):
    returnData = await request.json()
    return {"message": "submitted"}

@app.get("/recommendation")
def recommendation():
    return {"message": "recommendation"}

