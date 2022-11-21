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


ADDRESS_TO_WEBDRIVER = "/Users/sarahstevens/OneDrive/Documents/College/Fall 2022/CSCI4243W/LetsEat/LetsEat-Dev/yelp/chromedriver 9"
CLASS = "raw__09f24__T4Ezm"
DATABASE = r"ScrapedUserData.db"
occasions = ['date+night', 'friend','friends', 'family', 'clients', 'solo']
restrictionsList = ['vegan', 'vegetarian', 'gluten-free', 'kosher', 'pescatarian']


def get_reviews(yelpUrl, rest_id):

    for q in occasions+restrictionsList:
       
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
            [pos] BLOB,
            [neg] BLOB,
            [restrictions] BLOB,
            [occasion] NVARCHAR(50),
            [num_people] INTEGER,
            [meal] NVARCHAR(50),
            [price_range] NVARCHAR(50),
            [rest_id] NVARCHAR(50),
            [going] INTEGER)''')
        
        #close connection
        conn.commit()
        conn.close() 
    
        #print(yelpUrl+"&q="+q)
        
        #open chrome to scrape website
        driver = webdriver.Chrome(ADDRESS_TO_WEBDRIVER)
        driver.implicitly_wait(10)
        driver.get(yelpUrl+"?&q="+q)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2);
        
        
        #get days of week from scrape
        date = driver.find_elements(By.CLASS_NAME, "css-chan6m")
        dayOfWeek = []
        for i in range(len(date)):
            if date[i].text.find("/")!=-1:
                my_date = date[i].text
                datetime_object = datetime.strptime(my_date, '%m/%d/%Y')
                dayOfWeek.append(calendar.day_name[datetime_object.weekday()])  
    
        
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
                
                #fill database based on occasion/allergy
                review = lists[i].text.lower()
                current_day = dayOfWeek[i]
                business = YelpApiCalls.return_business(rest_id)
                
                #i currently add the categories listed, not our umbrella terms. will switch next sprint
                types = business.get('categories')
                pos = []
                for j in range(len(types)):
                    pos.append(types[j].get('alias'))
                neg = None
                restrictions = []
                
                if review.find('lunch') != -1:
                    meal = 'lunch'
                elif review.find('breakfast') != -1 or review.find('brunch') != -1 or review.find('morning') != -1:
                    meal = 'breakfast'
                else:
                    meal = 'dinner'
      
                occasion = None
                
                for res in restrictionsList:
                    if(review.find(res)!=-1 and res not in restrictions):
                        restrictions.append(res)
                
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
            
                            
                price = business.get('price')
                going = SentimentAnalysis(lists[i].text)
                
                #open connection 
                try:
                    conn = sqlite3.connect(DATABASE)
                    c = conn.cursor()
                except Error as e:
                    print(e)
                
                c.execute('INSERT INTO users (name, current_day, pos, neg, restrictions, occasion, num_people, meal, price_range, rest_id, going) VALUES((?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?))', 
                          (name,current_day, str(pos), neg, str(restrictions), occasion, num_people, meal, price, rest_id, going),)
        
                #close connection
                conn.commit()
                conn.close() 
    
    
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
    #print(score.get('compound'))
    if score.get('compound')>=.05:
        return 1
    else:
        return 0
    #print("{:-<65} {}".format(text, str(score)))

'''
positive sentiment: compound score >= 0.05
neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
negative sentiment: compound score <= -0.05

date night
friends
client

'''

