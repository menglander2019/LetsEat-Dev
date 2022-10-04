from fastapi import FastAPI
from backend.db.db_management import createUser

app = FastAPI()
 
@app.get("/")
def home():
    return {"message": "Hello World!"}

@app.get("/about")
def about():
    return {"message": "about"}

@app.get("/login")
def login():
    return {"message": "login page"}

@app.get("/signup")
def signup():
    return {"message": "signup page"}

@app.post("/signup/{user}-{pw}")
def signup(user, pw):
    createUser(user, pw)

@app.get("/createprofile")
def createprofile():
    return {"message": "createprofile"}

@app.get("/questionnaire")
def questionnaire():
    return {"message": "questionnaire"}

@app.get("/recommendation")
def recommendation():
    return {"message": "recommendation"}

