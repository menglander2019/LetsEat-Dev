import xgboost as xgb
import pandas as pd
import category_encoders as ce
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from feature_engine.encoding import DecisionTreeEncoder


rest_data_path = 'yelp/restaurantsTest.csv'
user_data_path = 'yelp/scrapedUsers.csv'

user_raw_data = pd.read_csv(user_data_path)
rest_raw_data = pd.read_csv(rest_data_path)

total_input = pd.merge(user_raw_data, rest_raw_data, on='rest_id')
total_input_cleaned = total_input.drop(['name', 'rest_id', 'website', 'going'], axis='columns')
output = total_input['going']

total_input_cleaned.to_csv('test.csv')

# trains the decision tree with randomly generated data and returns it along with its encoder
def train_dec_tree():
    # utilizes OneHotEncoder to convert categorical values
    onehot_encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoded_train_X = onehot_encoder.fit_transform(total_input_cleaned)

    # creates the decision tree classifier model and fits it to the converted training data
    dec_tree = xgb.XGBClassifier()
    dec_tree.fit(encoded_train_X, output)

    return [dec_tree, onehot_encoder]