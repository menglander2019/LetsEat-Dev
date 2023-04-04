import mysql.connector
from mysql.connector import Error
import random
import os
import bcrypt


config = {
    'host': 'letseatusersaws.cvfx18xhuald.us-east-1.rds.amazonaws.com',
    'database': 'users',
    'user': 'admin',
    'password':'$Cornucopia20037'
    # 'host':os.environ['DB_HOST'],
    # 'database':os.environ['DB_NAME'],
    # 'user':os.environ['DB_USER'],
    # 'password':os.environ['DB_PASSWORD'],
    # 'port':os.environ['DB_PORT']
}
# try:
mydb = mysql.connector.connect(**config)
#     cursor = cnx.cursor()
#     cursor.execute("SELECT * FROM userProfiles")
#     result = cursor.fetchall()
#     cursor.close()
#     cnx.close()
#     print(result)
# except mysql.connector.Error as err:
#     print(err)
# try:
#     if mydb.is_connected():
#         db_info = mydb.get_server_info()
#         print("Connected to MySQL Server Version ", db_info)
#         cursor = mydb.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

# except Error as e:
#     print("Error connecting to MySQL", e)
# finally:
#     if mydb.is_connected():
#         cursor.close()
#         mydb.close()
#         print("MySQL Connection is closed")

# mydb = mysql.connector.connect(host='localhost',
#                                         database='Users',
#                                         user='root',
#                                         password='Password')

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
    # first checks if the user exists and if they do, retrieves their salt
    c.execute('SELECT password FROM userProfiles WHERE email = %s', (email,))
    # if there is no result, then the user doesn't exist and False is returned
    salt = c.fetchone()
    if salt is None:
        return [0, 0]
    
    # Password is stored in the database as a 60 character string, the first 29 characters are the salt
    salt = salt[0]
    salt = salt[0:29]
    password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
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

def retrievePositives(id):
    c = mydb.cursor()
    # finds a user's preferences given their ID
    c.execute('SELECT positivePreferences FROM userPreferences WHERE userID = %s', (id,))

    result = c.fetchone()
    # returns the list of positive preferences for a given user's ID
    return result[0].split(',')

def retrieveNegatives(id):
    c = mydb.cursor()
    # finds a user's negative preferences given their ID
    c.execute('SELECT negativePreferences FROM userPreferences WHERE userID = %s', (id,))

    result = c.fetchone()
    # returns the list of negative preferences for a given user's ID
    return result[0].split(',')

def retrieveRestrictions(id):
    c = mydb.cursor()
    # finds a user's restrictions given their ID
    c.execute('SELECT restrictions FROM userPreferences WHERE userID = %s', (id,))

    result = c.fetchone()
    # returns the list of restrictions for a given user's ID
    return result[0].split(',')

def getNameByID(id):
    c = mydb.cursor()

    c.execute('SELECT name FROM userProfiles WHERE userID = %s', (id,))
    result = c.fetchone()

    return result[0]
