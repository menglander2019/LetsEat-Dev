import mysql.connector
import random

mydb = mysql.connector.connect(host='localhost',
                                         database='Users',
                                         user='root',
                                         password='196468maX!')

def createUser(user, pw):
    id = int(random.random() * 100000000)
    print(id)
    
    try:

        c = mydb.cursor()
        c.execute('SELECT * FROM userProfile WHERE userID = %s', (id,))
        result = c.fetchone()

        while result is not None:
            id = int(random.random() * 100000000)
            c.execute('SELECT * FROM userProfile WHERE userID = %s', (id,))
            result = c.fetchone()

        c.execute('SELECT * FROM userProfile WHERE email = %s', (user,))
        result = c.fetchone()

        if result is not None:
            return {"message": "ERROR: User already exists!"}

        user_insertion_query = "INSERT INTO userProfile VALUES (%s, %s, %s, %s, %s, %s)"
        record = (id, user, pw, '2000-01-01', 'man', 'bob')
        c.execute(user_insertion_query, record)
        mydb.commit()
        c.close
        return {"message": "User successfully created!"}
    except Exception as e:
        return {"message:": f"ERROR: {e}!"}