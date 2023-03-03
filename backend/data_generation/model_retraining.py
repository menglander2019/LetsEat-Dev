# Import writer class from csv module
from csv import writer
from backend.db.db_management import get_db
from restaurant_suggester import build_user_features, build_restaurant_features
from yelp.YelpApiCalls import return_business
import sqlite3
 
def create_new_row(userID, search_submission, restID, attended):
    # sets up database variables
    mydb = get_db()
    c = mydb.cursor()
    # fetch the user information from the database
    c.execute('SELECT positivePreferences, negativePreferences, restrictions FROM userPreferences WHERE userID = %s', (userID,))
    user_info = c.fetchone()
    positives = user_info[0].split(',')
    negatives = user_info[1].split(',')
    restrictions = user_info[2].split(',')
    user_cols = build_user_features(search_submission[0], search_submission[1], search_submission[2], search_submission[3], positives, negatives, restrictions)

    restaurant = return_business(restID)
    rest_cols = build_restaurant_features(restaurant)

    # opens up the scraped restaurant info database
    conn = sqlite3.connect("./yelp/OfficialRestaurantScraping.db")
    c = conn.cursor()

    c.execute("SELECT * FROM attributes WHERE restaurant_id = (?)", (restID,))
    result = c.fetchall()
    # if the restaurant is not found in the db, then something terribly wrong has happened (to get to this point the restaurant must have been found before in the ML code)
    if len(result) == 0:
        raise Exception("FATAL ERROR: Restaurant not found when re-training... this error should never occur...")

    scraped_info = list(result[0])[28:]

    # closes the connection to the sqlite3 db
    conn.close() 
    
    # appends the collected values based on the user profile, restaurant features (rating/price/cuisine), and the scraped restaurant values (and whether the user will attend)
    total_features = user_cols + rest_cols + scraped_info + [attended]
    return total_features

def append_user_input(row):
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('./backend/data_generation/random_data.csv', 'a', encoding='UTF8') as f:
        writer = writer(f)
        writer.writerow(row)
    
        f.close()