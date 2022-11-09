from fastapi import FastAPI
from backend.db.db_management import createUser
from backend.data_generation.data_gen_constants import cuisine_groups, restrictions_dict

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

@app.post("/signup/email/{email}/pw/{pw}/name/{name}/dob/{dob}/gender/{gender}/pos/{pos}/neg/{neg}/restr/{restr}")
def signup(email, pw, name, dob, gender, pos, neg, restr):
    return createUser(email, pw, name, dob, gender, pos, neg, restr)

@app.get("/profileQuestionInfo")
def getProfileQuestionInfo():
    return {
        "positives": cuisine_groups.keys(),
        "restrictions": restrictions_dict.keys(),
        "negatives": cuisine_groups.keys()
    }

@app.get("/createprofile")
def createprofile():
    return {"message": "createprofile"}

@app.get("/questionnaire")
def questionnaire():
    return {"message": "questionnaire"}

@app.get("/recommendation")
def recommendation():
    return {"message": "recommendation"}

