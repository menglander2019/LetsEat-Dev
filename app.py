from fastapi import FastAPI
from backend.dec_tree_tester import test_dec_tree
from backend.dec_tree_trainer import train_dec_tree
from yelp.YelpApiCalls import get_restaurant_list
from yelp.YelpWebscraping import scrape
import numpy

app = FastAPI()
 
@app.get("/")
def root ():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    dec_tree = train_dec_tree()
    user_features = test_dec_tree()
    restaurants = get_restaurant_list('20037', '4000', user_features[8], user_features[2])
    for restaurant in restaurants:
        temp_user_features = user_features
        id = restaurant.get('id')
        url = restaurant.get('url')
        scraped_info = scrape(id, url)
        category_list = restaurant.get('categories')
        categories = []
        for j in range(len(category_list)):
            categories.append(category_list[j].get('alias'))
        temp_user_features.append(','.join(categories))
        total_features = temp_user_features + list(scraped_info.values())
        print(total_features)
        print(restaurant.get('name') + " prediction: " + dec_tree.predict(numpy.array(total_features)))

    

