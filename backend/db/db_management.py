import mysql.connector
import random

mydb = mysql.connector.connect(host='localhost',
                                        database='Users',
                                        user='root',
                                        password='196468maX!')

def get_db():
    return mydb

# Database: Users
def createUser(email, pw, name, dob, gender):
    id = int(random.random() * 100000000)

    c = mydb.cursor()
    c.execute('SELECT * FROM userProfiles WHERE userID = %s', (id,))
    result = c.fetchone()

    while result is not None:
        id = int(random.random() * 100000000)
        c.execute('SELECT * FROM userProfiles WHERE userID = %s', (id,))
        result = c.fetchone()

    c.execute('SELECT * FROM userProfiles WHERE email = %s', (email,))
    result = c.fetchone()

    if result is not None:
        return {"message": "ERROR: User already exists!"}

    user_insertion_query = "INSERT INTO userProfiles VALUES (%s, %s, %s, %s, %s, %s)"
    # dob format: 2000-01-01
    user_record = (id, email, pw, dob, gender, name)
    c.execute(user_insertion_query, user_record)

    preference_insertion_query = "INSERT INTO userPreferences VALUES (%s, %s, %s, %s)"
    preference_record = (id, '', '', '')
    c.execute(preference_insertion_query, preference_record)

    mydb.commit()
    c.close()
    return {"message": "User successfully created!"}

def updatePositives(email, positives):
    c = mydb.cursor()
    # retrieves the user information based on the user who is logged in's email address
    c.execute('SELECT userID FROM userProfiles WHERE email = %s', (email,))
    id = c.fetchone()[0]
    # update the user's positive preferences in the database
    c.execute('UPDATE userPreferences SET positivePreferences = %s WHERE userID = %s', (positives, id))

    mydb.commit()
    c.close()

def updateNegatives(email, negatives):
    c = mydb.cursor()
    # retrieves the user information based on the user who is logged in's email address
    c.execute('SELECT userID FROM userProfiles WHERE email = %s', (email,))
    id = c.fetchone()[0]
    # update the user's negative preferences in the database
    c.execute('UPDATE userPreferences SET negativePreferences = %s WHERE userID = %s', (negatives, id))

    mydb.commit()
    c.close()

def updateRestrictions(email, restrictions):
    c = mydb.cursor()
    # retrieves the user information based on the user who is logged in's email address
    c.execute('SELECT userID FROM userProfiles WHERE email = %s', (email,))
    id = c.fetchone()[0]
    # update the user's negative preferences in the database
    c.execute('UPDATE userPreferences SET restrictions = %s WHERE userID = %s', (restrictions, id))

    mydb.commit()
    c.close()
