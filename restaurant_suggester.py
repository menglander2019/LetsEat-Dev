from backend.dec_tree_trainer import train_dec_tree
from yelp.YelpApiCalls import get_restaurant_list
from yelp.YelpWebscraping import scrape
from backend.data_generation.data_gen_constants import header, num_umbrella_terms, restaurant_types, days
from backend.db.db_management import get_db
from datetime import datetime
import numpy
import pandas as pd
import copy

def build_user_features(id, occasion, num_people, meal, price_ranges):
    mydb = get_db()
    c = mydb.cursor()
    # fetch the user information from the database
    c.execute('SELECT positivePreferences, negativePreferences, restrictions FROM userPreferences WHERE userID = %s', (id,))
    user_info = c.fetchone()
    positives = user_info[0].split(',')
    negatives = user_info[1].split(',')
    restrictions = user_info[2].split(',')

    print(positives)
    print(negatives)
    print(restrictions)

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
        rest_preferences[positive] = 1
    for negative in negatives:
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
    for restriction in restrictions:
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

def get_predictions(id, occasion, num_people, meal, price_ranges):
    # trains the decision tree and returns the tree along with the proper encoder
    dec_tree_info = train_dec_tree()
    dec_tree = dec_tree_info[0]
    encoder = dec_tree_info[1]
    # gets the user input for profile information (used for testing)
    user_features = build_user_features(id, occasion, num_people, meal, price_ranges)
    print(user_features)
    cuisines = []

    restaurants = get_restaurant_list('20037', '4000', price_range, ','.join(filter(None, cuisines)))
     # iterates through each restaurant, scraping data and making predictions
    for restaurant in restaurants:
        # temp_user_features = copy.deepcopy(user_features)
        temp_user_features = copy.copy(user_features)
        for value in user_features.values():
            temp_user_features += value

        id = restaurant.get('id')
        url = restaurant.get('url')
        scraped_info = scrape(id, url)
        # gets the rating of the restaurant
        rest_features = [restaurant.get('rating')]
        # gets the price of the restaurant and appends it to the list of restaurant features
        rest_prices = [0, 0, 0, 0]
        price = restaurant.get('price')
        rest_prices[len(price) - 1] = 1
        rest_features += rest_prices
        category_list = restaurant.get('categories')
        # iterates through each umbrella term to see if the scraped restaurant fits into that umbrella and sets to 1 if it finds it and 0 if not
        for type in restaurant_types.keys():
            found_type = False
            for category in category_list:
                if category.get('alias') in restaurant_types[type]:
                    found_type = True
            if found_type:
                rest_features.append(1)
            else:
                rest_features.append(0)
        
        # appends the collected values based on the user profile, restaurant features (rating/price/cuisine), and the scraped restaurant values
        total_features = numpy.array(temp_user_features + rest_features + list(scraped_info.values()))
        cols = {}
        # sets up a dataframe with the proper feature names and values
        for i in range(len(total_features)):
            cols[header[i+1]] = total_features[i]
        row = pd.DataFrame(data=cols, index=[0])
        row = row.astype('string')
        # encodes the categorical features using the encoder that trained the decision tree
        total_features_encoded = encoder.transform(row)
        # makes a prediction as to whether the user would attend this restaurant or not
        print(restaurant.get('name') + " prediction: " + str(dec_tree.predict_proba(total_features_encoded)))
        
if __name__ == "__main__":
    get_predictions(48017772, "date", 2, "dinner", [3, 4])