import sqlite3
from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


#These are the attributes relevant to the Machine Learning algorithm
ATTRIBUTES = ['Classy',
                  'Loud',
                  'Hipster',
                  'Groups',
                  'Kids',
                  'Garage',
                  'Street',
                  'Valet', 
                  'Validated',
                  'WiFi',
                  'Monday',
                  'Tuesday',
                  'Wednesday',
                  'Thursday',
                  'Friday',
                  'Saturday',
                  'Sunday',
                  'TV',
                  'Waiter',
                  'Outdoor',
                  'Dancing',
                  'Working',
                  'Smoking',
                  'Bike',
                  'Casual',
                  'Intimate',
                  'Upscale',
                  'Moderate',
                  'Quiet',
                  'Breakfast',
                  'Lunch',
                  'Dinner',
                  'Dessert',
                  'Brunch',
                  'Late',
                  'Trendy', 
                  'Divey',
                  'Bar',
                  'Catering',
                  'Plastic',    
                  'reusable',
                  'staffMasks',
                  'staffVac',
                  'vaccination',
                  'Compostable',
                  'Wheelchair',
                  'Vegan',
                  'Vegetarian',
                  'Gluten',
                  'Pescatarian',
                  'Keto',
                  'Soy',
                  'Dogs',
                  'Women',
                  'Military',
                  'Gender'
                  ]
#TRANSACTIONS?? ADD TO DB
DATABASE = r"OfficialRestaurantScraping.db"
TRUE_CLASS = "css-1p9ibgf"
FALSE_CLASS = "css-qyp8bo"
ADDRESS_TO_WEBDRIVER = "/Users/sarahstevens/OneDrive/Documents/College/Fall 2022/CSCI4243W/LetsEat/LetsEat-Dev/yelp/chromedriver 9"

#create database. this should not be called unless i accidently delete the database or we change it 
def createTable():
    
    #open connection
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    #create table
    c.execute('''CREATE TABLE IF NOT EXISTS attributes (
        [restaurant_id] NVARCHAR(50) PRIMARY KEY,
        [website] NVARCHAR(200), 
        [rating] FLOAT DEFAULT 0,
        [middle_eastern] INTEGER DEFAULT 0,
        [african] INTEGER DEFAULT 0,
        [american] INTEGER DEFAULT 0,
        [mexican] INTEGER DEFAULT 0,
        [latin_american] INTEGER DEFAULT 0,
        [italian] INTEGER DEFAULT 0,
        [chinese] INTEGER DEFAULT 0,
        [japanese] INTEGER DEFAULT 0,
        [southern_central_asian] INTEGER DEFAULT 0,
        [french] INTEGER DEFAULT 0,
        [eastern_europe] INTEGER DEFAULT 0,
        [central_europe] INTEGER DEFAULT 0,
        [caribbean] INTEGER DEFAULT 0,
        [mediterranean] INTEGER DEFAULT 0,
        [indian] INTEGER DEFAULT 0,
        [spanish] INTEGER DEFAULT 0,
        [kosher] INTEGER DEFAULT 0,
        [gluten_free] INTEGER DEFAULT 0,
        [oneDollar] INTEGER DEFAULT 0,
        [twoDollar] INTEGER DEFAULT 0,
        [threeDollar] INTEGER DEFAULT 0,
        [fourDollar] INTEGER DEFAULT 0,
        [pickup] INTEGER DEFAULT 0,
        [delivery] INTEGER DEFAULT 0,
        [restaurant_reservation] INTEGER DEFAULT 0) ''')
    
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
def scrape(rest_id, url, categories, price, rating, transaction):
    print("Scraping " + rest_id)
    #open connection 
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
    except Error as e:
        print(e)

    #add restaurant to database
    c.execute('INSERT INTO attributes (restaurant_id) VALUES((?))', (rest_id,))
    
    #add cuisine type (umbrella terms) to database
    for j in range(len(categories)):
        alias = categories[j]
        c.execute('''UPDATE attributes
            SET '''+alias+''' = 1
            WHERE restaurant_id = (?);''',
            (rest_id, )) 

    #add whether they do delviery, pickup, or reservations to database
    for j in range(len(transaction)):
        alias = transaction[j]
        c.execute('''UPDATE attributes
            SET '''+alias+''' = 1
            WHERE restaurant_id = (?);''',
            (rest_id, )) 
    
    #determine price and add to database
    if price == '$':
        sqlprice = 'oneDollar'
        c.execute('''UPDATE attributes
            SET '''+sqlprice+''' = 1
            WHERE restaurant_id = (?);''',
            (rest_id,))  
    if price == '$$':
        sqlprice = 'twoDollar' 
        c.execute('''UPDATE attributes
            SET '''+sqlprice+''' = 1
            WHERE restaurant_id = (?);''',
            (rest_id,))     
    if price == '$$$':
        sqlprice = 'threeDollar'  
        c.execute('''UPDATE attributes
            SET '''+sqlprice+''' = 1
            WHERE restaurant_id = (?);''',
            (rest_id,))    
    if price == '$$$$$':
        sqlprice = 'fourDollar'    
        c.execute('''UPDATE attributes
                SET '''+sqlprice+''' = 1
                WHERE restaurant_id = (?);''',
                (rest_id,))  

    #add rating to database
    c.execute('''UPDATE attributes
        SET rating = '''+str(rating)+'''
        WHERE restaurant_id = (?);''',
        (rest_id,))  

    #open chrome to scrape website
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ADDRESS_TO_WEBDRIVER, chrome_options=options)
    driver.get(url)
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
            searchAttribute = ATTRIBUTES[j]
            if(ATTRIBUTES[j] == 'WiFi'):
                searchAttribute = 'Wi-Fi'
            elif(ATTRIBUTES[j] == 'staffMasks'):
                searchAttribute = 'Staff wears masks'
            elif(ATTRIBUTES[j] == 'staffVac'):
                searchAttribute = 'All staff fully vaccinated'

            if searchAttribute in all_pos_attributes[i].text:
                c.execute('''UPDATE attributes
                          SET '''+ATTRIBUTES[j]+''' = 1
                          WHERE restaurant_id = (?);''',
                          (rest_id,))  
                          
    #search for attributes the restaurant does not have
    all_neg_attributes = driver.find_elements(By.CLASS_NAME, FALSE_CLASS)
    for j in range(len(ATTRIBUTES)):
        for i in range(len(all_neg_attributes)):
            #update database so attribute as -1
            searchAttribute = ATTRIBUTES[j]

            if(ATTRIBUTES[j] == 'WiFi'):
                searchAttribute = 'Wi-Fi'
            elif(ATTRIBUTES[j] == 'staffMasks'):
                searchAttribute = 'Staff wears masks'
            elif(ATTRIBUTES[j] == 'staffVac'):
                searchAttribute = 'All staff fully vaccinated'

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

    #write to csv
    clients = pd.read_sql('SELECT * FROM attributes' ,conn)
    clients.to_csv('restaurantsTest.csv', index=False)
    
    #close connection 
    conn.commit()
    conn.close() 


#createTable()
def main(business_id, url, categories, price, rating, transactions):
    if(checkExistance(business_id)==False):
        scrape(business_id, url, categories, price, rating, transactions)
        #printDB()
        return True
    else:
        #printDB()
        return False
    
