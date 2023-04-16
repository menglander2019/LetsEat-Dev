# Import writer class from csv module
from csv import writer
from backend.db.db_management import get_db
from backend.data_generation.data_gen_constants import days
from yelp.YelpApiCalls import return_business
from ..db.db_management import retrievePositives, retrieveNegatives, retrieveRestrictions
from datetime import datetime
import sqlite3
 
def create_new_row(userID, search_submission, restID, attended):
    dt = datetime.now()
    current_day = days[dt.weekday()]
    # sets up database variables
    mydb = get_db()
    c = mydb.cursor()
    # fetch the user information from the database
    positives = retrievePositives(userID)
    negatives = retrieveNegatives(userID)
    restrictions = retrieveRestrictions(userID)

    c.execute('SELECT name from userProfiles WHERE userID = %s', (userID,))
    user_name = c.fetchone()[0]

    c.close()

    user_retraining_dict = {
        "name": user_name,
        "current_day": current_day,
        "middle_eastern": 0,
        "african": 0,
        "american": 0,
        "mexican": 0,
        "latin_american": 0,
        "italian": 0,
        "chinese": 0,
        "japanese": 0,
        "southern_central_asian": 0,
        "french": 0,
        "eastern_europe": 0,
        "central_europe": 0,
        "caribbean": 0,
        "mediterranean": 0,
        "indian": 0,
        "spanish": 0,
        "kosher": 0,
        "gluten_free": 0,
        "wheelchair": 0,
        "vegan": 0,
        "vegetarian": 0,
        "pescatarian": 0,
        "keto": 0,
        "soy": 0,
        "dog": 0,
        "covid": 0,
        "occasion": search_submission[0],
        "num_people": search_submission[1],
        "meal": search_submission[2],
        "oneDollar": 0,
        "twoDollar": 0,
        "threeDollar": 0,
        "fourDollar": 0,
        "rest_id": restID,
        "going": attended,
    }

    for positive in positives:
        if positive not in user_retraining_dict:
            raise Exception("FATAL ERROR: user cuisine preference not found in retraining headers...")
        user_retraining_dict[positive] = 1
    for negative in negatives:
        if negative not in user_retraining_dict:
            raise Exception("FATAL ERROR: user cuisine dislike not found in retraining headers...")
        user_retraining_dict[negative] = -1
    for restriction in restrictions:
        if restriction == '':
            continue
        if restriction not in user_retraining_dict:
            raise Exception("FATAL ERROR: user dietary restriction not found in retraining headers...")
        user_retraining_dict[restriction] = 1

    price_ranges = search_submission[3]
    for price in price_ranges:
        if price == 1:
            user_retraining_dict["oneDollar"] = 1
        elif price == 2:
            user_retraining_dict["twoDollar"] = 1
        elif price == 3: 
            user_retraining_dict["threeDollar"] = 1
        elif price == 4:
            user_retraining_dict["fourDollar"] = 1

    return user_retraining_dict.values()

def append_user_input(row):
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('./yelp/scrapedUsers.csv', 'a', encoding='UTF8') as f:
        f_writer = writer(f)
        f_writer.writerow(row)
    
        f.close()