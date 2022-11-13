from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from backend.db.db_management import createUser

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

question = [
    {
        "id": "q1",
        "question": "Example Question",
        "answerChoices": ["One", "Two", "Three"],
        "selectedChoices": []
    },
    {
        "id": "q2",
        "question": "Example Question 2",
        "answerChoices": ["One", "Two", "Four"],
        "selectedChoices": []
    }

]
 
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

@app.get("/questionnaire/profile")
def questionnaire_profile():
    return {"data": question}

@app.post("/submit/questionnaire/")
def submit_questionnaire():
    return {"message": "submitted"}

@app.get("/questionnaire/search/")
def questionnaire_search():
    return {"data": question}

@app.post("/submit/search/")
def submit_search():
    return {"message": "submitted"}

@app.get("/recommendation")
def recommendation():
    return {"message": "recommendation"}

