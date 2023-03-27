try:
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import boto3
    import csv
    import calendar
    from io import StringIO
    from datetime import datetime
    import time
    import random
    import pandas as pd
    from selenium.webdriver.common.keys import Keys
    print("All Modules are ok ...")

except Exception as e:
    print("Error in Imports ")
    
    
occasions = ['date+night', 'friend','friends', 'family', 'clients', 'solo']
restrictionsList = ['vegan', 'vegetarian', 'gluten-free', 'kosher', 'wheelchair', 'pescatarian', 'keto', 'soy', 'dog', 'covid']



class WebDriver(object):

    def __init__(self):
        self.options = Options()

        self.options.binary_location = '/opt/headless-chromium'
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')

    def get(self):
        driver = Chrome('/opt/chromedriver', options=self.options)
        return driver
        

def scrape(driver, q, rest_id, url, categories, price, rating, transaction):

    #get days of week from scrape
    #TODO
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

    full_dict = []
    #interate reviews
    for i in range(len(lists)):
        
        name = people[i+1].text
        #if(checkExistance(name) == False):  #TODO CHECKEXISTENCE
            
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
        #price = business.get('price')

        #determine if they would attend
        #going = SentimentAnalysis(lists[i].text)    #TODO

        import boto3
        comprehend = boto3.client("comprehend")
        sa = comprehend.detect_sentiment(Text = lists[i].text, LanguageCode="en")
        print(sa)

        going=1
        if sa["Sentiment"] == "NEGATIVE":
            going = 0
        else:
            going=1
        
        rest_dict = {
            'restaurant_id': rest_id,
            'name': name,
            'current_day': current_day,
            'middle_eastern': 0,
            'african': 0,
            'american': 0,
            'mexican': 0,
            'latin_american': 0,
            'italian': 0,
            'chinese': 0,
            'japanese': 0,
            'southern_central_asian': 0,
            'french': 0,
            'eastern_europe': 0,
            'central_europe': 0,
            'caribbean': 0,
            'mediterranean': 0,
            'indian': 0,
            'spanish': 0,
            'kosher': 0,
            'gluten_free': 0,
            'wheelchair': 0,
            'vegan': 0,
            'vegetarian': 0,
            'pescatarian': 0,
            'keto': 0,    
            'soy': 0,
            'dog': 0,
            'covid': 0,
            'occasion': occasion,
            'num_people': num_people,
            'meal': meal,        
            'oneDollar': 0,
            'twoDollar': 0,
            'threeDollar': 0,
            'fourDollar': 0,
            'going': going,
            'review': lists[i].text
        }
        

        #add price preference to database
        if price == '$':
            sqlprice = 'oneDollar'
            rest_dict[sqlprice] = 1 
            
        if price == '$$':
            sqlprice = 'twoDollar'  
            rest_dict[sqlprice] = 1    
            
        if price == '$$$':
            sqlprice = 'threeDollar'   
            rest_dict[sqlprice] = 1 
            
        if price == '$$$$':
            sqlprice = 'fourDollar'    
            rest_dict[sqlprice] = 1  

        #add umbrella term to databasw
        #types = business.get('categories')
        #categories = YelpApiCalls.cuisines_to_umbrellas(types)      #TODO
        for j in range(len(categories)):
            alias = categories[j]
            rest_dict[alias] = 1 

        #add restrictions to database
        for restriction in restrictions:
            updRestriction = restriction
            if restriction == 'gluten-free':
                updRestriction = 'gluten_free'
            rest_dict[updRestriction] = 1   

        full_dict.append(rest_dict)
    return full_dict

def upload_csv_s3(data_dictionary,s3_bucket_name,csv_file_name):
    data_dict = data_dictionary
    data_dict_keys = data_dictionary[0].keys()
    
    # creating a file buffer
    file_buff = StringIO()
    
    # writing csv data to file buffer
    writer = csv.DictWriter(file_buff, fieldnames=data_dict_keys)
    writer.writeheader()
    for data in data_dict:
        writer.writerow(data)
        
    # creating s3 client connection
    client = boto3.client('s3')
    
    # placing file to S3, file_buff.getvalue() is the CSV body for the file
    client.put_object(Body=file_buff.getvalue(), Bucket=s3_bucket_name, Key=csv_file_name)
    #print('Done uploading to S3')

def lambda_handler(event, context):
    instance_ = WebDriver()
    driver = instance_.get()
    driver.get(event.get('url')+"?&q="+event.get('query'))   #CHECK THIS
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    #print('Fetching the page')
    

    table_data = scrape(driver, event['query'], event['rest_id'], event['url'], event['categories'], event['price'], event['rating'], event['transaction'])
    
    driver.close()
    driver.quit()
    
    #create csv and upload in s3 bucket
    dt_string = datetime.now().strftime("%Y-%m-%d_%H%M")
    csv_file_name =  'restaurant'+event.get('rest_id')+'at'+dt_string +'.csv'
    upload_csv_s3(table_data,'scrapedreviews',csv_file_name)

    response = {
        "Rows": len(table_data),
        "body": table_data
    }

    return response

