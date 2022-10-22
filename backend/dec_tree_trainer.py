import xgboost as xgb
import pandas as pd
import category_encoders as ce
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from feature_engine.encoding import DecisionTreeEncoder


data_path = '/Users/maxenglander/Documents/2022-23_School_Shit/FALL/SD/LetsEat-Dev/random_data.csv'
raw_data = pd.read_csv(data_path)

le = LabelEncoder()

input = raw_data.drop(['name', 'ATTEND?'], axis='columns')
output = raw_data['ATTEND?']

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = train_test_split(input, output, test_size=0.25, random_state=0)

    encoder = ce.HashingEncoder(cols=['+', '-', 'cuisine', 'current_day', 'restrictions', 'occasion', 'meal', 'price_range'])
    encoder.fit(X_train, y_train)
    cleaned_train_x = encoder.transform(X_train)
    cleaned_test_x = encoder.transform(X_test)

    # encoder = DecisionTreeEncoder(random_state=0)
    # encoder.fit(X_train, y_train)

    # train_t = encoder.transform(X_train)
    # test_t = encoder.transform(X_test)

    # print(train_t)

    dec_tree = xgb.XGBClassifier()
    dec_tree.fit(cleaned_train_x, y_train)

    print("DEC TREE Accuracy: " + str(dec_tree.score(cleaned_test_x, y_test)))