from backend.dec_tree_trainer import train_dec_tree
from backend.matrix_factorization_trainer import train_matrix_factorization
from yelp.YelpApiCalls import get_restaurant_list
from yelp.YelpWebscraping import scrape
from backend.data_generation.data_gen_constants import header, num_umbrella_terms, restaurant_types
import numpy
import category_encoders as ce
import pandas as pd
import copy

offline_rest_info = [{'id': 'U0tfep9yNBASTe2zAG6cPw', 'alias': 'filomena-ristorante-washington', 'name': 'Filomena Ristorante', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/t7Y783V7AOjQCKnfMW1TmQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/filomena-ristorante-washington?adjust_creative=zQXigI7LgZAT12wMOc08kg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=zQXigI7LgZAT12wMOc08kg', 'review_count': 3070, 'categories': [{'alias': 'italian', 'title': 'Italian'}, {'alias': 'wine_bars', 'title': 'Wine Bars'}], 'rating': 4.0, 'coordinates': {'latitude': 38.90443, 'longitude': -77.062546}, 'transactions': ['pickup', 'delivery'], 'price': '$$$', 'location': {'address1': '1063 Wisconsin Ave NW', 'address2': '', 'address3': '', 'city': 'Washington, DC', 'zip_code': '20007', 'country': 'US', 'state': 'DC', 'display_address': ['1063 Wisconsin Ave NW', 'Washington, DC 20007']}, 'phone': '+12023388800', 'display_phone': '(202) 338-8800', 'distance': 782.3818771776953}, {'id': 'CW59Vd9CLC6atVHkK-aHUQ', 'alias': 'sfoglina-rosslyn-arlington-2', 'name': 'Sfoglina Rosslyn', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/jqjxe6mSR5RtzbakXh_7bw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/sfoglina-rosslyn-arlington-2?adjust_creative=zQXigI7LgZAT12wMOc08kg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=zQXigI7LgZAT12wMOc08kg', 'review_count': 180, 'categories': [{'alias': 'italian', 'title': 'Italian'}, {'alias': 'desserts', 'title': 'Desserts'}, {'alias': 'wineries', 'title': 'Wineries'}], 'rating': 4.0, 'coordinates': {'latitude': 38.894573, 'longitude': -77.070168}, 'transactions': [], 'price': '$$$', 'location': {'address1': '1100 Wilson Blvd', 'address2': '', 'address3': None, 'city': 'Arlington', 'zip_code': '22209', 'country': 'US', 'state': 'VA', 'display_address': ['1100 Wilson Blvd', 'Arlington, VA 22209']}, 'phone': '+12025251402', 'display_phone': '(202) 525-1402', 'distance': 1161.35799673629}, {'id': 'hIDsn0pPz_rxqOfnnB1q2g', 'alias': 'sfoglina-downtown-washington', 'name': 'Sfoglina - Downtown', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/j0stHLJygkTueBH6k43rYQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/sfoglina-downtown-washington?adjust_creative=zQXigI7LgZAT12wMOc08kg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=zQXigI7LgZAT12wMOc08kg', 'review_count': 216, 'categories': [{'alias': 'italian', 'title': 'Italian'}], 'rating': 4.0, 'coordinates': {'latitude': 38.90157, 'longitude': -77.02669}, 'transactions': ['delivery'], 'price': '$$$', 'location': {'address1': '1099 New York Ave NW', 'address2': '', 'address3': None, 'city': 'Washington, DC', 'zip_code': '20001', 'country': 'US', 'state': 'DC', 'display_address': ['1099 New York Ave NW', 'Washington, DC 20001']}, 'phone': '+12025251402', 'display_phone': '(202) 525-1402', 'distance': 2718.4947887161707}, {'id': 'Qc09Y-P78XX6n8cyL3Kf6w', 'alias': 'mele-bistro-arlington-3', 'name': 'Mele Bistro', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/0b_4KLZm-fSSqMpRk7Ts9Q/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/mele-bistro-arlington-3?adjust_creative=zQXigI7LgZAT12wMOc08kg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=zQXigI7LgZAT12wMOc08kg', 'review_count': 479, 'categories': [{'alias': 'french', 'title': 'French'}, {'alias': 'italian', 'title': 'Italian'}, {'alias': 'cocktailbars', 'title': 'Cocktail Bars'}], 'rating': 4.0, 'coordinates': {'latitude': 38.89419, 'longitude': -77.07889}, 'transactions': ['pickup', 'delivery'], 'price': '$$$', 'location': {'address1': '1723 Wilson Blvd', 'address2': None, 'address3': '', 'city': 'Arlington', 'zip_code': '22209', 'country': 'US', 'state': 'VA', 'display_address': ['1723 Wilson Blvd', 'Arlington, VA 22209']}, 'phone': '+17035225222', 'display_phone': '(703) 522-5222', 'distance': 1869.4062033761445}, {'id': 'KAlEMleKomiXDmE7wDOZeA', 'alias': 'al-tiramisu-washington', 'name': 'Al Tiramisu', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/jJbC13VBSF8yjL1wxipV3w/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/al-tiramisu-washington?adjust_creative=zQXigI7LgZAT12wMOc08kg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=zQXigI7LgZAT12wMOc08kg', 'review_count': 431, 'categories': [{'alias': 'italian', 'title': 'Italian'}], 'rating': 4.0, 'coordinates': {'latitude': 38.9093919, 'longitude': -77.04557}, 'transactions': ['delivery'], 'price': '$$$', 'location': {'address1': '2014 P St NW', 'address2': '', 'address3': '', 'city': 'Washington, DC', 'zip_code': '20036', 'country': 'US', 'state': 'DC', 'display_address': ['2014 P St NW', 'Washington, DC 20036']}, 'phone': '+12024674466', 'display_phone': '(202) 467-4466', 'distance': 1626.1629024849683}]
offline_scraped_info = ['T' 'italian' '' '' 'date' '2' 'dinner' '3' 'italian,wine_bars' '1' '1'
 '1' '1' '1' '1' '0' '0' '0' '0' '0' '1' '1' '1' '1' '-1' '-1' '-1' '-1'
 '-1' '1' '0' '0' '0' '1' '0' '0' '0' '0' '0' '1']

def get_inputs():
    day = input("What's the current day?\n")
    positive1 = input("What cuisines do you prefer?\n")
    positive2 = input("What cuisines do you prefer?\n")
    positive3 = input("What cuisines do you prefer?\n")
    positive4 = input("What cuisines do you prefer?\n")
    positive5 = input("What cuisines do you prefer?\n")
    negative1 = input("What cuisines do you dislike?\n")
    negative2 = input("What cuisines do you dislike?\n")
    negative3 = input("What cuisines do you dislike?\n")
    negative4 = input("What cuisines do you dislike?\n")
    negative5 = input("What cuisines do you dislike?\n")
    restrictions = input("Any dietary restrictions?\n")
    occasion = input("What is the occasion?\n")
    if occasion == "solo":
        num_people = 1
    elif occasion == "date":
        num_people = 2
    else:
        num_people = int(input("How many people will be going?\n"))
    meal = input("What meal will it be for?\n")
    price_range = input("What is your price range?\n")

    cuisine_preferences = {}
    for i in range(num_umbrella_terms):
        cuisine_preferences[header[i+2]] = 0

    if positive1 in cuisine_preferences:
        cuisine_preferences[positive1] = 1
    if positive2 in cuisine_preferences:
        cuisine_preferences[positive2] = 1
    if positive3 in cuisine_preferences:
        cuisine_preferences[positive3] = 1
    if positive4 in cuisine_preferences:
        cuisine_preferences[positive4] = 1
    if positive5 in cuisine_preferences:
        cuisine_preferences[positive5] = 1

    if negative1 in cuisine_preferences:
        cuisine_preferences[negative1] = -1
    if negative2 in cuisine_preferences:
        cuisine_preferences[negative2] = -1
    if negative3 in cuisine_preferences:
        cuisine_preferences[negative3] = -1
    if negative4 in cuisine_preferences:
        cuisine_preferences[negative4] = -1
    if negative5 in cuisine_preferences:
        cuisine_preferences[negative5] = -1

    return [day] + list(cuisine_preferences.values()) + [restrictions, occasion, num_people, meal, price_range]


if __name__ == "__main__":
    # # trains the decision tree and returns the tree along with the proper encoder
    # dec_tree_info = train_dec_tree()
    # dec_tree = dec_tree_info[0]
    # encoder = dec_tree_info[1]

    # trains matrix factorization model
    m_fact = train_matrix_factorization()

    # gets the user input for profile information (used for testing)
    user_features = get_inputs()
    cuisines = []
    # searches through the positive preferences and adds them to the list of cuisines the user wants
    for i in range(1, num_umbrella_terms+1):
        if user_features[i] == 1:
            cuisines.append(header[i+1])
    restaurants = get_restaurant_list('20037', '4000', user_features[21], ','.join(filter(None, cuisines)))
     # iterates through each restaurant, scraping data and making predictions
    for restaurant in restaurants:
        temp_user_features = copy.deepcopy(user_features)
        id = restaurant.get('id')
        url = restaurant.get('url')
        scraped_info = scrape(id, url)
        category_list = restaurant.get('categories')
        categories = []
        # iterates through each umbrella term to see if the scraped restaurant fits into that umbrella and sets to 1 if it finds it and 0 if not
        for type in restaurant_types.keys():
            found_type = False
            for category in category_list:
                if category.get('alias') in restaurant_types[type]:
                    found_type = True
            if found_type:
                temp_user_features.append(1)
            else:
                temp_user_features.append(0)
        # appends the collected values based on the user profile and the scraped restaurant values
        total_features = numpy.array(temp_user_features + list(scraped_info.values()))
        cols = {}
        # sets up a dataframe with the proper feature names and values
        for i in range(len(total_features)):
            cols[header[i+1]] = total_features[i]
        row = pd.DataFrame(data=cols, index=[0])
        row = row.astype('string')
        # encodes the categorical features using the encoder that trained the decision tree
        # total_features_encoded = encoder.transform(row)
        # # makes a prediction as to whether the user would attend this restaurant or not
        # print(restaurant.get('name') + " prediction: " + str(dec_tree.predict(total_features_encoded)))

        # makes a prediction using matrix factorization model
        print(restaurant.get('name') + " prediction: " + str(m_fact.predict(row)))
        