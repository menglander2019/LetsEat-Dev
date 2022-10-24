import sqlite3
from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.common.by import By

#These are the attributes relevant to the Machine Learning algorithm
ATTRIBUTES = ['Classy',
                  'Loud',
                  'Groups',
                  'Kids',
                  'Garage',
                  'Street', 
                  'WiFi',
                  'Monday',
                  'Tuesday',
                  'Wednesday',
                  'Thursday',
                  'Friday',
                  'Saturday',
                  'Sunday',
                  'TV',
                  'Outdoor',
                  'Dancing',
                  'Working',
                  'Smoking',
                  'Bike',
                  'Casual',
                  'Moderate',
                  'Breakfast',
                  'Lunch',
                  'Dinner',
                  'Dessert',
                  'Brunch',
                  'Late',
                  'Trendy', 
                  'Divey',
                  'Bar']

DATABASE = r"YelpScrapeData.db"
TRUE_CLASS = "css-1p9ibgf"
FALSE_CLASS = "css-qyp8bo"
ADDRESS_TO_WEBDRIVER = "/Users/sarahstevens/OneDrive/Documents/College/Fall 2022/CSCI4243W/LetsEat/LetsEat-Dev/yelp/chromedriver 6"

#create database. this should not be called unless i accidently delete the database or we change it 
def createTable():
    
    #open connection
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    #create table
    c.execute('''CREATE TABLE IF NOT EXISTS attributes (
        [restaurant_id] NVARCHAR(50) PRIMARY KEY,
        [website] NVARCHAR(50) )''')
    
    #add column for each attribute
    for i in range(len(ATTRIBUTES)):
        c.execute('''ALTER TABLE attributes ADD COLUMN ''' + ATTRIBUTES[i] + ''' INTEGER DEFAULT 0''')
    
    #close connection
    conn.commit()
    conn.close() 
    
#check if the restaurant is already in our database and returns True or False
def checkExistance(rest_id):
    
    #open connection
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
    except Error as e:
        print(e)
        
    #select restaurant from table
    c.execute("SELECT * FROM attributes WHERE restaurant_id = (?)", (rest_id,))
    result = c.fetchall()
    
    #close connections
    conn.commit()
    conn.close() 
    
    #return whether we found the list
    if(result == []):
        return False
    return True

    
#adds the restaurant to our database and queries attributes to add to database and add website
def scrape(rest_id, url):
 
    #open chrome to scrape website
    driver = webdriver.Chrome(ADDRESS_TO_WEBDRIVER)
    driver.get(url)
    
    #open connection 
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
    except Error as e:
        print(e)

    #add restaurant to database
    c.execute('INSERT INTO attributes (restaurant_id) VALUES((?))', (rest_id,))

    #access attributes by clicking button on yelp page
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for i in range(len(buttons)):
        if("More Attributes" in buttons[i].text):
            buttons[i].click()

    #search for attributes the restaurant has
    all_pos_attributes = driver.find_elements(By.CLASS_NAME, TRUE_CLASS)
    for j in range(len(ATTRIBUTES)):
        for i in range(len(all_pos_attributes)):
            #update database so attribute as 1
            if ATTRIBUTES[j] in all_pos_attributes[i].text:
                c.execute('''UPDATE attributes
                          SET '''+ATTRIBUTES[j]+''' = 1
                          WHERE restaurant_id = (?);''',
                          (rest_id,))  
                          
    #search for attributes the restaurant does not have
    all_neg_attributes = driver.find_elements(By.CLASS_NAME, FALSE_CLASS)
    for j in range(len(ATTRIBUTES)):
        for i in range(len(all_neg_attributes)):
            #update database so attribute as -1
            if ATTRIBUTES[j] in all_neg_attributes[i].text:
                c.execute('''UPDATE attributes
                          SET '''+ATTRIBUTES[j]+''' = -1
                          WHERE restaurant_id = (?);''',
                          (rest_id,))  

    #search for website on yelp page
    siteForDB = url
    try:
        website = driver.find_element(By.PARTIAL_LINK_TEXT, "http://")
        siteForDB = website.text
    except:
        try:
            website = driver.find_element(By.PARTIAL_LINK_TEXT, "https://")
            siteForDB = website.text
        except:
            #if website is not found, add yelp url to database
            print("Cannot retrieve website")
       
    #add url to website column of database 
    c.execute('''UPDATE attributes
              SET website = (?)
              WHERE restaurant_id = (?);''',
              (siteForDB, rest_id,)) 
    
    #close connection
    conn.commit()
    conn.close() 
    
#prints contents of database FOR TESTING ONLY 
def printDB():
    
    #open connection
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
    except Error as e:
        print(e)
        
    #select contents
    c.execute("SELECT * FROM attributes")
    result = c.fetchall()
  
    #print results 
    for r in range(len(result)):
        print(result[r])
        print("\n")
    
    #close connection 
    conn.commit()
    conn.close() 


createTable()
def main(business_id, url):
    if(checkExistance(business_id)==False):
        scrape(business_id, url)
    #printDB()
