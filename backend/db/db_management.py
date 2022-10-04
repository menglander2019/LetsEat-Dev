import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                                         database='Users',
                                         user='root',
                                         password='196468maX!')

def createUser(user, pw):
    c = mydb.cursor()
    user_insertion_query = "INSERT INTO userProfile (username, password) VALUES (%s, %s)"
    record = (user, pw)
    c.execute(user_insertion_query, record)
    mydb.commit()
    c.close