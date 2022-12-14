import mysql.connector
import random
import os

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

def updatePositives(id, positives_list):
    c = mydb.cursor()
    # update the user's positive preferences in the database
    positives = ','.join(positives_list)
    print(positives)
    c.execute('UPDATE userPreferences SET positivePreferences = %s WHERE userID = %s', (positives, id))

    mydb.commit()
    c.close()

def updateNegatives(id, negatives_list):
    c = mydb.cursor()
    # update the user's negative preferences in the database
    negatives = ','.join(negatives_list)
    print(negatives)
    c.execute('UPDATE userPreferences SET negativePreferences = %s WHERE userID = %s', (negatives, id))

    mydb.commit()
    c.close()

def updateRestrictions(id, restrictions_list):
    c = mydb.cursor()
    # update the user's negative preferences in the database
    restrictions = ','.join(restrictions_list)
    print(restrictions)
    c.execute('UPDATE userPreferences SET restrictions = %s WHERE userID = %s', (restrictions, id))

    mydb.commit()
    c.close()

def checkUser(email, password):
    c = mydb.cursor()
    # finds a user's ID given their email and password
    c.execute('SELECT userID FROM userProfiles WHERE email = %s AND password = %s', (email, password))

    result = c.fetchone()
    # if there is no result, then the user doesn't exist and False is returned, True is returned otherwise
    if result is None:
        return [0, 0]
    return [1, result[0]]

def checkNewUser(id):
    c = mydb.cursor()
    # finds a user's preferences given their ID
    c.execute('SELECT positivePreferences, negativePreferences, restrictions FROM userPreferences WHERE userID = %s', (id,))

    result = c.fetchone()
    # returns 1 if the user has no preferences set yet
    if result[0] == '' and result[1] == '' and result[2] == '':
        return 1
    # returns 0 if the user has any of their preferences set up
    return 0