try:
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import boto3
    import csv
    from io import StringIO
    from datetime import datetime
    import time
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    print("All Modules are ok ...")

except Exception as e:
    print("Error in Imports ")
    
TRUE_CLASS = "css-1p9ibgf"
FALSE_CLASS = "css-qyp8bo"   
    
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
        

def scrape(driver, rest_id, url, categories, price, rating, transaction):

    rest_dict = {
    'restaurant_id': rest_id,
    'website': 0,
    'rating': 0,
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
    'oneDollar': 0,
    'twoDollar': 0,
    'threeDollar': 0,
    'fourDollar': 0,
    'pickup': 0,
    'delivery': 0,
    'restaurant_reservation': 0,
    'Classy': 0,
    'Loud': 0,
    'Hipster': 0,
    'Groups': 0,
    'Kids': 0,
    'Garage': 0,
    'Street': 0,
    'Valet': 0, 
    'Validated': 0,
    'WiFi': 0,
    'Monday': 0,
    'Tuesday': 0,
    'Wednesday': 0,
    'Thursday': 0,
    'Friday': 0,
    'Saturday': 0,
    'Sunday': 0,
    'TV': 0,
    'Waiter': 0,
    'Outdoor': 0,
    'Dancing': 0,
    'Working': 0,
    'Smoking': 0,
    'Bike': 0,
    'Casual': 0,
    'Intimate': 0,
    'Upscale': 0,
    'Moderate': 0,
    'Quiet': 0,
    'Breakfast': 0,
    'Lunch': 0,
    'Dinner': 0,
    'Dessert': 0,
    'Brunch': 0,
    'Late': 0,
    'Trendy': 0, 
    'Divey': 0,
    'Bar': 0,
    'Catering': 0,
    'Plastic': 0,    
    'reusable': 0,
    'staffMasks': 0,
    'staffVac': 0,
    'vaccination': 0,
    'Compostable': 0,
    'Wheelchair': 0,
    'Vegan': 0,
    'Vegetarian': 0,
    'Gluten': 0,
    'Pescatarian': 0,
    'Keto': 0,
    'Soy': 0,
    'Dogs': 0,
    'Women': 0,
    'Military': 0,
    'Gender': 0
    }
    
    #add cuisine type (umbrella terms) to database
    for j in range(len(categories)):
        alias = categories[j]
        rest_dict[alias] = 1
        
    #add transaction types to db
    for j in range(len(transaction)):
        alias = transaction[j]
        rest_dict[alias] = 1
        
    #determine price and add to database
    if price == '$':
        sqlprice = 'oneDollar'
        rest_dict[sqlprice] = 1 
        
    elif price == '$$':
        sqlprice = 'twoDollar' 
        rest_dict[sqlprice] = 1 
        
    elif price == '$$$':
        sqlprice = 'threeDollar'  
        rest_dict[sqlprice] = 1 
        
    elif price == '$$$$$':
        sqlprice = 'fourDollar'    
        rest_dict[sqlprice] = 1 
        
    #add rating
    rest_dict['rating'] = str(rating)
    
    print("Scraping Beginnning uh hello")
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2);
    
    #WebDriverWait wait = new WebDriverWait (driver, 30)
    #wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//button[contains(text(),'More Attributes')]"))).click()
    #("")
    #wait = WebDriverWait(driver, 30)
    #element = wait.until(EC.element_to_be_clickable(By.XPATH, "//button[contains(text,'More Attributes')]"))
    #element.click()
    
    '''   
    #access attributes by clicking button on yelp page
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for button in ((buttons)):
        print(button.text)
        if("More Attributes" in button.text):
            print("button clicked")
            print(button.click())   #NOT WORKING
            #button.send_keys(Keys.ENTER)
            break
    '''
    
    try:
        alert = driver.switch_to.alert
        alert.dismiss()
    except:
        print("No Alert")
        pass
    
    #access attributes by clicking button on yelp page
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for button in ((buttons)):
        print(button.text)
        if("More Attributes" in button.text):
            #wait = WebDriverWait(driver, 30)
            #element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, str(button.id))))
            print(button.click())
            #driver.execute_script("arguments[0].click();", button)
            
            print("BRUHHHH", button.get_attribute('disabled'))
            break


    
    all_pos_attributes = driver.find_elements(By.CLASS_NAME, TRUE_CLASS)
    for i in range(len(all_pos_attributes)):
        print("pos:", all_pos_attributes[i].text)
        for j in range(len(ATTRIBUTES)):
            #update database so attribute as 1
            searchAttribute = ATTRIBUTES[j]
            if(ATTRIBUTES[j] == 'WiFi'):
                searchAttribute = 'Wi-Fi'
            elif(ATTRIBUTES[j] == 'staffMasks'):
                searchAttribute = 'Staff wears masks'
            elif(ATTRIBUTES[j] == 'staffVac'):
                searchAttribute = 'All staff fully vaccinated'

            if searchAttribute in all_pos_attributes[i].text:
                rest_dict[ATTRIBUTES[j]] = 1
    '''  
    #search for attributes the restaurant does not have
    all_neg_attributes = driver.find_elements(By.CLASS_NAME, FALSE_CLASS)
    for i in range(len(all_neg_attributes)):
        for j in range(len(ATTRIBUTES)):
            #print(all_neg_attributes[i].text)
            #update database so attribute as -1
            searchAttribute = ATTRIBUTES[j]

            if(ATTRIBUTES[j] == 'WiFi'):
                searchAttribute = 'Wi-Fi'
            elif(ATTRIBUTES[j] == 'staffMasks'):
                searchAttribute = 'Staff wears masks'
            elif(ATTRIBUTES[j] == 'staffVac'):
                searchAttribute = 'All staff fully vaccinated'

            if ATTRIBUTES[j] in all_neg_attributes[i].text:
                rest_dict[ATTRIBUTES[j]] = -1    

    '''
    return rest_dict

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
    print('Done uploading to S3')

def lambda_handler(event, context):
    instance_ = WebDriver()
    driver = instance_.get()
    driver.get(event.get('url'))   #CHECK THIS
    print('Fetching the page')

    table_data = [scrape(driver, event['rest_id'], event['url'], event['categories'], event['price'], event['rating'], event['transaction'])]
    
    driver.close()
    driver.quit()
    
    #create csv and upload in s3 bucket
    dt_string = datetime.now().strftime("%Y-%m-%d_%H%M")
    csv_file_name =  'restaurant'+event['rest_id']+'at'+dt_string +'.csv'
    upload_csv_s3(table_data,'scrapedrestaurants',csv_file_name)

    response = {
        "Rows": 1,
        "body": table_data
    }


    return response

