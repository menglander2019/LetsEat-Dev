import mysql.connector
import random

#mydb = mysql.connector.connect(host='localhost',
#                                         database='Users',
#                                         user='root',
#                                         password='196468maX!')

# Database: Users
def createUser(email, pw, name, dob, gender, pos, neg, restr):
    id = int(random.random() * 100000000)
    
    try:
        c = mydb.cursor()
        c.execute('SELECT * FROM userProfile WHERE userID = %s', (id,))
        result = c.fetchone()

        while result is not None:
            id = int(random.random() * 100000000)
            c.execute('SELECT * FROM userProfile WHERE userID = %s', (id,))
            result = c.fetchone()

        c.execute('SELECT * FROM userProfile WHERE email = %s', (email,))
        result = c.fetchone()

        if result is not None:
            return {"message": "ERROR: User already exists!"}

        user_insertion_query = "INSERT INTO userProfile VALUES (%s, %s, %s, %s, %s, %s)"
        # dob format: 2000-01-01
        user_record = (id, email, pw, dob, gender, name)
        c.execute(user_insertion_query, user_record)

        preference_insertion_query = "INSERT INTO userPreferences VALUES (%s, %s, %s, %s)"
        preference_record = (id, pos, neg, restr)
        c.execute(preference_insertion_query, preference_record)

        mydb.commit()
        c.close
        return {"message": "User successfully created!"}
    except Exception as e:
        return {"message:": f"ERROR: {e}!"}