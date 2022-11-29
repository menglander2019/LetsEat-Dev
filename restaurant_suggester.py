from backend.dec_tree_trainer import train_dec_tree
from yelp.YelpApiCalls import get_restaurant_list
from yelp.YelpWebscraping import scrape, DATABASE
from backend.data_generation.data_gen_constants import header, num_umbrella_terms, restaurant_types, days
from backend.db.db_management import get_db
from datetime import datetime
import numpy
import pandas as pd
import copy
import time
import sqlite3

def build_user_features(occasion, num_people, meal, price_ranges, positives, negatives, restrictions):
    # gets the current day
    dt = datetime.now()
    current_day = days[dt.weekday()]

    # create a dictionary that represents likes and dislikes of user, with each val set to 0
    rest_preferences = {
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
        'spanish': 0
    }
    # iterate through positives and set any matching to 1, same with negatives but -1
    for positive in positives:
        if positive not in rest_preferences:
            raise Exception("ERROR: Invalid cuisine preference for given user")
        rest_preferences[positive] = 1
    for negative in negatives:
        if negative not in rest_preferences:
            raise Exception("ERROR: Invalid cuisine preference for given user")
        rest_preferences[negative] = -1
    # converts the restauraunt preferences to a list
    rest_preferences = list(rest_preferences.values())
    
    # a dictionary representing each possible restriction a user could input
    restriction_settings = {
        'kosher': 0, 
        'gluten_free': 0, 
        'wheelchair': 0, 
        'vegan': 0, 
        'vegetarian': 0, 
        'pescatarian': 0, 
        'keto': 0, 
        'soy': 0, 
        'dog': 0, 
        'covid': 0
    }
    # iterates through the restrictions the user chose and assigns a value of 1 to it
    print(restrictions)
    for restriction in restrictions:
        if restriction == '':
            continue
        elif restriction not in restriction_settings:
            raise Exception("ERROR: Invalid dietary restriction for given user")
        restriction_settings[restriction] = 1
    # converts the restrictions settings into a list
    restriction_settings = list(restriction_settings.values())

    # creates the list of possible price_ranges
    prices = [0, 0, 0, 0]
    for price in price_ranges:
        # subtracts each value of price by 1 because the indexes start at 0 (price of 1 should make the 0th index = 1)
        prices[price - 1] = 1

    # combine all accumulated data and return it
    return [current_day] + rest_preferences + restriction_settings + [occasion, num_people, meal] + prices

def build_restaurant_features(restaurant):
    # gets the rating of the restaurant
    rating = restaurant.get('rating')
    # gets the categories for each restaurant        
    category_list = restaurant.get('categories')
    category_features = []
    kosher_and_gluten_free = [0, 0]
    # iterates through each umbrella term to see if the scraped restaurant fits into that umbrella and sets to 1 if it finds it and 0 if not
    for type in restaurant_types.keys():
        found_type = False
        for category in category_list:
            # if a restaurant is kosher it is recorded
            if category.get('alias') == 'kosher':
                kosher_and_gluten_free[0] = 1
            # if a restaurant is gluten free it is recorded
            elif category.get('alias') == 'gluten_free':
                kosher_and_gluten_free[1] = 1
            # if the category is found within the major categories, then set the flag to true and append
            elif category.get('alias') in restaurant_types[type]:
                found_type = True
        if found_type:
            category_features.append(1)
        else:
            category_features.append(0)

    # gets the price of the restaurant and appends it to the list of restaurant features
    rest_prices = [0, 0, 0, 0]
    price = restaurant.get('price')
    # prices are in the format $$$, so the length of this subtracted by 1 gives the index of the proper price
    rest_prices[len(price) - 1] = 1

    # determines if the restaurant offers pickup/delivery/reservation options
    transactions = restaurant.get('transactions')
    pickup_delivery_reservation = [0, 0, 0]
    if 'pickup' in transactions:
        pickup_delivery_reservation[0] = 1
    if 'delivery' in transactions:
        pickup_delivery_reservation[1] = 1
    if 'restaurant_reservation' in transactions:
        pickup_delivery_reservation[2] = 1

    return [rating] + category_features + kosher_and_gluten_free + rest_prices + pickup_delivery_reservation
    
def make_prediction(restaurant, user_features, encoder, dec_tree):
    print("Making prediction for:", restaurant.get('name'))
    temp_user_features = copy.copy(user_features)
    rest_features = build_restaurant_features(restaurant)
            
    # retrieves the restaurant ID and url so that the scraped info can be retrieved
    rest_id = restaurant.get('id')
    url = restaurant.get('url')

    # opens up the scraped restaurant info database
    conn = sqlite3.connect("./yelp/OfficialRestaurantScraping.db")
    c = conn.cursor()

    c.execute("SELECT * FROM attributes WHERE restaurant_id = (?)", (rest_id,))
    result = c.fetchall()
    # for now, if the restaurant is not in the db then skip it and return 0 (in the future, the scrape call should go here)
    if len(result) == 0:
        print("The restaurant was not in the db!")
        return 0
    print(list(result[0])[28:])
    
    #scraped_info = list(scrape(rest_id, url)).values()
    scraped_info = list(result[0])[28:]
    print("length:", len(scraped_info))

    # closes the connection to the sqlite3 db
    conn.close() 
    
    # appends the collected values based on the user profile, restaurant features (rating/price/cuisine), and the scraped restaurant values
    total_features = temp_user_features + rest_features + scraped_info
    cols = {}
    # sets up a dataframe with the proper feature names and values
    for i in range(len(total_features)):
        cols[header[i+1]] = total_features[i]
    row = pd.DataFrame(data=cols, index=[0])
    # encodes the categorical features using the encoder that trained the decision tree
    total_features_encoded = encoder.transform(row)
    # makes a prediction as to whether the user would attend this restaurant or not
    prediction_prob = dec_tree.predict_proba(total_features_encoded)[0]
    print("Prediction prob for " + str(restaurant.get('name')) + " is= " + str(prediction_prob))
    # if the model has an above 50% confidence score that the restaurant should be suggested, return the value
    if prediction_prob[1] > 0.5:
        return prediction_prob[1]
    # if the confidence score is too low, return 0 to indicate that the restaurant shouldn't be suggested
    return 0

def get_predictions(id, occasion, num_people, meal, price_ranges, zip):
    # trains the decision tree and returns the tree along with the proper encoder
    start_time = time.time()
    dec_tree_info = train_dec_tree()
    print("Training time:", time.time() - start_time)

    dec_tree = dec_tree_info[0]
    encoder = dec_tree_info[1]

    # sets up database variables
    mydb = get_db()
    c = mydb.cursor()
    # fetch the user information from the database
    c.execute('SELECT positivePreferences, negativePreferences, restrictions FROM userPreferences WHERE userID = %s', (id,))
    user_info = c.fetchone()
    positives = user_info[0].split(',')
    negatives = user_info[1].split(',')
    restrictions = user_info[2].split(',')

    # gets the user input for profile information (used for testing)
    user_features = build_user_features(occasion, num_people, meal, price_ranges, positives, negatives, restrictions)
    cuisines = user_info[0]
    restaurants = get_restaurant_list(zip, '4000', price_ranges, cuisines)
    print(f"FOUND {len(restaurants)} restaurants!")
    # iterates through each restaurant, scraping data and making predictions
    suggestions_list = []
    start_time = time.time()
    for restaurant in restaurants:
        suggestion = make_prediction(restaurant, user_features, encoder, dec_tree)
        # if the model predicts a suggestion, then append it to the unordered dictionary as a key-value pair
        if suggestion > 0:
            suggestions_list.append([restaurant, suggestion])
    
    # edge-case: no restaurants are found, so an empty list is returned
    if len(suggestions_list) == 0:
        return []

    suggestions_sorted = sorted(suggestions_list, key=lambda x: x[1])
    suggestions_sorted_list = list(numpy.array(suggestions_sorted)[:,0])
    print("Total prediction time:", time.time() - start_time)
    print("Final list of sorted predicted restaurants:", suggestions_sorted_list)

    return suggestions_sorted_list

if __name__ == "__main__":
    get_predictions(48017772, "Date", 2, "Dinner", [3,4])