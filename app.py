from fastapi import FastAPI
from backend.dec_tree_tester import test_dec_tree
from backend.dec_tree_trainer import train_dec_tree
from yelp.YelpApiCalls import get_restaurant_list
from yelp.YelpWebscraping import scrape
import numpy
import category_encoders as ce
import pandas as pd

offline_rest_info = [{'id': 'U0tfep9yNBASTe2zAG6cPw', 'alias': 'filomena-ristorante-washington', 'name': 'Filomena Ristorante', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/t7Y783V7AOjQCKnfMW1TmQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/filomena-ristorante-washington?adjust_creative=zQXigI7LgZAT12wMOc08kg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=zQXigI7LgZAT12wMOc08kg', 'review_count': 3070, 'categories': [{'alias': 'italian', 'title': 'Italian'}, {'alias': 'wine_bars', 'title': 'Wine Bars'}], 'rating': 4.0, 'coordinates': {'latitude': 38.90443, 'longitude': -77.062546}, 'transactions': ['pickup', 'delivery'], 'price': '$$$', 'location': {'address1': '1063 Wisconsin Ave NW', 'address2': '', 'address3': '', 'city': 'Washington, DC', 'zip_code': '20007', 'country': 'US', 'state': 'DC', 'display_address': ['1063 Wisconsin Ave NW', 'Washington, DC 20007']}, 'phone': '+12023388800', 'display_phone': '(202) 338-8800', 'distance': 782.3818771776953}, {'id': 'CW59Vd9CLC6atVHkK-aHUQ', 'alias': 'sfoglina-rosslyn-arlington-2', 'name': 'Sfoglina Rosslyn', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/jqjxe6mSR5RtzbakXh_7bw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/sfoglina-rosslyn-arlington-2?adjust_creative=zQXigI7LgZAT12wMOc08kg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=zQXigI7LgZAT12wMOc08kg', 'review_count': 180, 'categories': [{'alias': 'italian', 'title': 'Italian'}, {'alias': 'desserts', 'title': 'Desserts'}, {'alias': 'wineries', 'title': 'Wineries'}], 'rating': 4.0, 'coordinates': {'latitude': 38.894573, 'longitude': -77.070168}, 'transactions': [], 'price': '$$$', 'location': {'address1': '1100 Wilson Blvd', 'address2': '', 'address3': None, 'city': 'Arlington', 'zip_code': '22209', 'country': 'US', 'state': 'VA', 'display_address': ['1100 Wilson Blvd', 'Arlington, VA 22209']}, 'phone': '+12025251402', 'display_phone': '(202) 525-1402', 'distance': 1161.35799673629}, {'id': 'hIDsn0pPz_rxqOfnnB1q2g', 'alias': 'sfoglina-downtown-washington', 'name': 'Sfoglina - Downtown', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/j0stHLJygkTueBH6k43rYQ/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/sfoglina-downtown-washington?adjust_creative=zQXigI7LgZAT12wMOc08kg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=zQXigI7LgZAT12wMOc08kg', 'review_count': 216, 'categories': [{'alias': 'italian', 'title': 'Italian'}], 'rating': 4.0, 'coordinates': {'latitude': 38.90157, 'longitude': -77.02669}, 'transactions': ['delivery'], 'price': '$$$', 'location': {'address1': '1099 New York Ave NW', 'address2': '', 'address3': None, 'city': 'Washington, DC', 'zip_code': '20001', 'country': 'US', 'state': 'DC', 'display_address': ['1099 New York Ave NW', 'Washington, DC 20001']}, 'phone': '+12025251402', 'display_phone': '(202) 525-1402', 'distance': 2718.4947887161707}, {'id': 'Qc09Y-P78XX6n8cyL3Kf6w', 'alias': 'mele-bistro-arlington-3', 'name': 'Mele Bistro', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/0b_4KLZm-fSSqMpRk7Ts9Q/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/mele-bistro-arlington-3?adjust_creative=zQXigI7LgZAT12wMOc08kg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=zQXigI7LgZAT12wMOc08kg', 'review_count': 479, 'categories': [{'alias': 'french', 'title': 'French'}, {'alias': 'italian', 'title': 'Italian'}, {'alias': 'cocktailbars', 'title': 'Cocktail Bars'}], 'rating': 4.0, 'coordinates': {'latitude': 38.89419, 'longitude': -77.07889}, 'transactions': ['pickup', 'delivery'], 'price': '$$$', 'location': {'address1': '1723 Wilson Blvd', 'address2': None, 'address3': '', 'city': 'Arlington', 'zip_code': '22209', 'country': 'US', 'state': 'VA', 'display_address': ['1723 Wilson Blvd', 'Arlington, VA 22209']}, 'phone': '+17035225222', 'display_phone': '(703) 522-5222', 'distance': 1869.4062033761445}, {'id': 'KAlEMleKomiXDmE7wDOZeA', 'alias': 'al-tiramisu-washington', 'name': 'Al Tiramisu', 'image_url': 'https://s3-media1.fl.yelpcdn.com/bphoto/jJbC13VBSF8yjL1wxipV3w/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/al-tiramisu-washington?adjust_creative=zQXigI7LgZAT12wMOc08kg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=zQXigI7LgZAT12wMOc08kg', 'review_count': 431, 'categories': [{'alias': 'italian', 'title': 'Italian'}], 'rating': 4.0, 'coordinates': {'latitude': 38.9093919, 'longitude': -77.04557}, 'transactions': ['delivery'], 'price': '$$$', 'location': {'address1': '2014 P St NW', 'address2': '', 'address3': '', 'city': 'Washington, DC', 'zip_code': '20036', 'country': 'US', 'state': 'DC', 'display_address': ['2014 P St NW', 'Washington, DC 20036']}, 'phone': '+12024674466', 'display_phone': '(202) 467-4466', 'distance': 1626.1629024849683}]
offline_scraped_info = ['T' 'italian' '' '' 'date' '2' 'dinner' '3' 'italian,wine_bars' '1' '1'
 '1' '1' '1' '1' '0' '0' '0' '0' '0' '1' '1' '1' '1' '-1' '-1' '-1' '-1'
 '-1' '1' '0' '0' '0' '1' '0' '0' '0' '0' '0' '1']

app = FastAPI()
 
@app.get("/")
def root ():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    dec_tree_info = train_dec_tree()
    dec_tree = dec_tree_info[0]
    encoder = dec_tree_info[1]
    user_features = test_dec_tree()
    # restaurants = get_restaurant_list('20037', '4000', user_features[7], user_features[1])
    restaurants = offline_rest_info
    # print("FOR OFFLINE:")
    # print(restaurants)
    # print("DONE OFFLINE")
    for restaurant in restaurants:
        try:
            # temp_user_features = user_features
            # id = restaurant.get('id')
            # url = restaurant.get('url')
            # scraped_info = scrape(id, url)
            # category_list = restaurant.get('categories')
            # categories = []
            # for j in range(len(category_list)):
            #     categories.append(category_list[j].get('alias'))
            # temp_user_features.append(','.join(categories))
            # total_features = numpy.array(temp_user_features + list(scraped_info.values()))
            # total_features = ['T', 'italian', '', '', 'date', '2', 'dinner', '3', 'italian,wine_bars', '1', '1', 
            #                             '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '-1', '-1', '-1', '-1',
            #                             '-1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1']       
            total_features = numpy.array([['T', 'italian', '', '', 'date', '2', 'dinner', '3', 'italian,wine_bars', '1', '1', 
                                          '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '-1', '-1', '-1', '-1',
                                          '-1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1']])
            # cols = {'current_day': total_features[0], '+': total_features[1], '-': total_features[2], 'restrictions': total_features[3], 'occasion': total_features[4], 'num_people': int(total_features[5]), 'meal': total_features[6], 'price_range': int(total_features[7]), 'cuisine': total_features[8], 'Classy': int(total_features[9]), 'Loud': int(total_features[10]), 'Moderate': int(total_features[11]), 'Groups': int(total_features[12]), 'Kids': int(total_features[13]), 'Garage': int(total_features[14]), 'Street': int(total_features[15]), 'WiFi': int(total_features[16]), 'Monday': int(total_features[17]), 'Tuesday': int(total_features[18]), 'Wednesday': int(total_features[19]), 'Thursday': int(total_features[20]), 'Friday': int(total_features[21]), 'Saturday': int(total_features[22]), 'Sunday': int(total_features[23]), 'TV': int(total_features[24]), 'Outdoor': int(total_features[25]), 'Dancing': int(total_features[26]), 'Working': int(total_features[27]), 'Smoking': int(total_features[28]), 'Bike': int(total_features[29]), 'Casual': int(total_features[30]), 'Breakfast': int(total_features[31]), 'Lunch': int(total_features[32]), 'Dinner': int(total_features[33]), 'Dessert': int(total_features[34]), 'Brunch': int(total_features[35]), 'Late': int(total_features[36]), 'Trendy': int(total_features[37]), 'Divey': int(total_features[38]), 'Bar': int(total_features[39])}
            # df = pd.DataFrame(data=cols, index=[0])
            # #df.loc[len(df)] = total_features
            # print(df)
            total_features_encoded = encoder.transform(total_features)
            print(total_features_encoded)
            print(restaurant.get('name') + " prediction: " + dec_tree.predict(total_features_encoded, output_margin=False, validate_features=True))
        except Exception as e:
            print("EXCEPTION: " + str(e))
            break

    

