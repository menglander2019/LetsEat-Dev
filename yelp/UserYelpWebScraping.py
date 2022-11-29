from . import YelpApiCalls
import sqlite3
from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import calendar
import time
import random
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import threading

ADDRESS_TO_WEBDRIVER = "/Users/sarahstevens/OneDrive/Documents/College/Fall 2022/CSCI4243W/LetsEat/LetsEat-Dev/yelp/chromedriver 9"
CLASS = "raw__09f24__T4Ezm"
DATABASE = r"OfficialUserScraping.db"
occasions = ['date+night', 'friend','friends', 'family', 'clients', 'solo']
restrictionsList = ['vegan', 'vegetarian', 'gluten-free', 'kosher', 'wheelchair', 'pescatarian', 'keto', 'soy', 'dog', 'covid']

thread_list = list()

def get_reviews(yelpUrl, rest_id, business):
    # Start test
    for q in occasions+restrictionsList:
        t = threading.Thread(name='Test '+q, target=get_reviews2, args=(yelpUrl, rest_id, q, business))
        t.start()
        time.sleep(1)
        print(t.name + ' started!')
        thread_list.append(t)

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    print('Test completed!')


def get_reviews2(yelpUrl, rest_id, q, business):
       
       #open connection 
        try:
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
        except Error as e:
            print(e)
            
         #create table
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            [name] NVARCHAR(50) PRIMARY KEY,
            [current_day] NVARCHAR(50),
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
            [wheelchair] INTEGER DEFAULT 0,
            [vegan] INTEGER DEFAULT 0,
            [vegetarian] INTEGER DEFAULT 0,
            [pescatarian] INTEGER DEFAULT 0,
            [keto] INTEGER DEFAULT 0,
            [soy] INTEGER DEFAULT 0,
            [dog] INTEGER DEFAULT 0,
            [covid] INTEGER DEFAULT 0,
            [occasion] NVARCHAR(50),
            [num_people] INTEGER,
            [meal] NVARCHAR(50),
            [oneDollar] INTEGER DEFAULT 0,
            [twoDollar] INTEGER DEFAULT 0,
            [threeDollar] INTEGER DEFAULT 0,
            [fourDollar] INTEGER DEFAULT 0,
            [rest_id] NVARCHAR(50),
            [going] INTEGER)''')
        
        #close connection
        conn.commit()
        conn.close() 
        
        #open chrome to scrape website
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(ADDRESS_TO_WEBDRIVER, chrome_options=options)
        driver.implicitly_wait(10)
        driver.get(yelpUrl+"?&q="+q)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2);
        
        
        #get days of week from scrape
        date = driver.find_elements(By.CLASS_NAME, "css-chan6m")
        dayOfWeek = []
        for i in range(len(date)):
            if date[i].text.find("/")!=-1:
                try:
                    my_date = date[i].text
                    datetime_object = datetime.strptime(my_date, '%m/%d/%Y')
                    dayOfWeek.append(calendar.day_name[datetime_object.weekday()])  
                except ValueError:
                    print("Time error")
                    dayOfWeek.append("Saturday")
    
        
        #get text reviews and peoples names 
        lists = driver.find_elements(By.XPATH, "//section[@aria-label='Recommended Reviews']//p[@class='comment__09f24__gu0rG css-qgunke']")
        people = driver.find_elements(By.XPATH, "//section[@aria-label='Recommended Reviews']//a[@role='link']")

        '''
        #just for testing
        if(len(lists)<2):
            temp = len(lists)
        else:
            temp = 2
        '''
        
        temp = len(lists)
    
        #interate reviews
        for i in range(temp):
            
            name = people[i+1].text
            if(checkExistance(name) == False):
                
                #get data from review
                review = lists[i].text.lower()
                current_day = dayOfWeek[i]
                #business = YelpApiCalls.return_business(rest_id)
                restrictions = []
                
                #determine if its bfast, lunch, or dinner
                if review.find('lunch') != -1:
                    meal = 'lunch'
                elif review.find('breakfast') != -1 or review.find('brunch') != -1 or review.find('morning') != -1:
                    meal = 'breakfast'
                else:
                    meal = 'dinner'
      
                occasion = None
                
                #find occasions in review
                for res in restrictionsList:
                    if(review.find(res)!=-1 and res not in restrictions):
                        restrictions.append(res)
                
                #find restrictions in review
                if q in restrictionsList:
                    for occ in occasions:
                        if review.find(' ' + occ.replace('+', ' ') + ' ') != -1:
                            q = occ
                                
                if q == "date+night":
                    occasion = 'date'
                    num_people = 2
                            
                elif q=='solo':
                    occasion = 'solo'
                    num_people = '1'
                            
                elif q=='friend':
                    occasion = 'friends'
                    num_people = 2
                            
                elif q=='friends':
                    occasion = 'friends'
                    num_people = random.randint(3,10)
                            
                elif q == 'family':
                    occasion = 'family'
                    num_people = random.randint(2,10)
    
                elif q == 'clients':
                    occasion = 'clients'
                    num_people = random.randint(2,10)
                else:
                    occasion = None
                    num_people = None
            
                #get price       
                price = business.get('price')

                #determine if they would attend
                going = SentimentAnalysis(lists[i].text)
                
                
                try:
                    #open connection 
                    try:
                        conn = sqlite3.connect(DATABASE)
                        c = conn.cursor()
                    except Error as e:
                        print(e)  
                    #create row
                    c.execute('INSERT INTO users (name, current_day, occasion, num_people, meal, rest_id, going) VALUES((?), (?), (?), (?), (?), (?), (?))', 
                            (name,current_day, occasion, num_people, meal, rest_id, going),)

                    #add price preference to database
                    if price == '$':
                        sqlprice = 'oneDollar'
                        c.execute('''UPDATE users
                            SET '''+sqlprice+''' = 1
                            WHERE name = (?);''',
                            (name,))  
                    if price == '$$':
                        sqlprice = 'twoDollar'  
                        c.execute('''UPDATE users
                                SET '''+sqlprice+''' = 1
                                WHERE name = (?);''',
                                (name,))    
                    if price == '$$$':
                        sqlprice = 'threeDollar'   
                        c.execute('''UPDATE users
                            SET '''+sqlprice+''' = 1
                            WHERE name = (?);''',
                            (name,))   
                    if price == '$$$$':
                        sqlprice = 'fourDollar'    
                        c.execute('''UPDATE users
                                SET '''+sqlprice+''' = 1
                                WHERE name = (?);''',
                                (name,))  

                    #add umbrella term to databasw
                    types = business.get('categories')
                    categories = YelpApiCalls.cuisines_to_umbrellas(types)
                    for j in range(len(categories)):
                        alias = categories[j]
                        c.execute('''UPDATE users
                            SET '''+alias+''' = 1
                            WHERE name = (?);''',
                            (name, )) 

                    #add restrictions to database
                    for restriction in restrictions:
                        updRestriction = restriction
                        if restriction == 'gluten-free':
                            updRestriction = 'gluten_free'
                        c.execute('''UPDATE users
                            SET '''+updRestriction+''' = 1
                            WHERE name = (?);''',
                            (name, ))   
                    #close connection
                    conn.commit()
                    conn.close() 
                except Error as e:
                    print(e)
        
    #printDB()
    
#print database, FOR TESTING
def printDB():
    
    #open connection
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
    except Error as e:
        print(e)
        
    #select contents
    c.execute("SELECT * FROM users")
    result = c.fetchall()
  
    #print results 
    for r in range(len(result)):
        print(result[r])
        print("\n")

    #write to csv
    clients = pd.read_sql('SELECT * FROM users' ,conn)
    clients.to_csv('scrapedUsers.csv', index=False)
    
    #close connection 
    conn.commit()
    conn.close() 
    
#check if name has already been added
def checkExistance(name):
    
    #open connection
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
    except Error as e:
        print(e)
        
    #select restaurant from table
    c.execute("SELECT * FROM users WHERE name = (?)", (name,))
    result = c.fetchall()
    
    #close connections
    conn.commit()
    conn.close() 
    
    #return whether we found the list
    if(result == []):
        return False
    return True

def SentimentAnalysis(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)

    if score.get('compound')>=.05:
        return 1
    else:
        return 0

'''
positive sentiment: compound score >= 0.05
neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
negative sentiment: compound score <= -0.05


'''

