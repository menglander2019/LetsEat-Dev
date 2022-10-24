import requests
from .YelpWebscraping import *
from datetime import datetime
import time

API_KEY= "NIeApqUv-eXDl1Uk9Lp1tdYbkmwQqlAWIrE87BI6ntY1RAktDOUG2nadraL9hYnRr6qMDPwcanx4c_A_qKOZykBQmP4gmvpOe61Q4lPxLnejZc8VFxWEnBv4haYwY3Yx"

headers = {
    'Authorization': 'Bearer %s' % API_KEY,
}
API_URL = "https://api.yelp.com/v3/businesses/search"
 
#iterate json results and add each restaurant to db
def updateDB(response):
    businesses = response.get('businesses')
    for i in range(len(businesses)):
        YelpWebscraping.main(businesses[i].get('id'), businesses[i].get('url'))

#get list of restaurants based on parameters
def request_businesses_list(zipcode, distance, dollars, open_at, categories, attributes):

    #convert time to UNIX
    #now = datetime(2022, 10, 13, 12, 20)
    now = datetime.now()
    unix = time.mktime(now.timetuple())
    
    #add parameters to API call
    params = {
        'term': 'restaurants',
        'location': zipcode,
        'radius': distance,
        'price': dollars,
        'open_at': str(int(unix)),
        'categories': categories,
        'attributes': attributes,
        'limit': 5
    }
    
    #request API data
    response = requests.request('GET', API_URL, headers=headers, params=params)
    
    #add restaurants from API call to webscraping db
    #updateDB(response.json())

    return response.json()

#print results FOR TESTING
def parse_results(businesses):

    for i in range(len(businesses)):
        print(businesses[i].get('name'))
        print("Business ID: "+businesses[i].get('id'))
        print("Distance from you: "+ str(float(businesses[i].get('distance'))/1609.344))
        print("Rating: " + str(businesses[i].get('rating')))
        print("Price: "+ businesses[i].get('price'))
        print("Url: "+ businesses[i].get('url'))
        print("Categories: ")
        list = businesses[i].get('categories')
        for j in range(len(list)):
            print("\t"+list[j].get('alias'))
        print("Location: ")
        for j in (businesses[i].get('location').get('display_address')):
            print("\t"+j)
        print()
    #YelpWebscraping.printDB()

#use businessId to get json results for that business
def return_business(businessId):
    url = 'https://api.yelp.com/v3/businesses/'+businessId
    response = requests.request('GET', url, headers=headers, params=None)
    return response.json()
    

def get_restaurant_list(zip, dist, price_range, cuisines):
    #this is test code. in real life, request_businesses_list is directly called
    zipcode = zip
    distance = dist #in meters, cannot exeed 4000
    dollars = price_range
    open_at = '1664468447' #in unix nums 
    categories = cuisines
    attributes = None
    
    response = request_businesses_list(zipcode, distance, dollars, open_at, categories, attributes)
    
    #print results to verify
    businesses = response.get('businesses')
    parse_results(businesses)
    return businesses
    

if __name__ == '__main__':
    print("stop that")
