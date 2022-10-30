import xgboost as xgb
import pandas as pd
import category_encoders as ce
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from feature_engine.encoding import DecisionTreeEncoder


data_path = '/Users/maxenglander/Documents/2022-23_School_Shit/FALL/SD/LetsEat-Dev/random_data.csv'
raw_data = pd.read_csv(data_path)

le = LabelEncoder()

input = raw_data.drop(['name', 'ATTEND?'], axis='columns')
output = raw_data['ATTEND?']

# trains the decision tree with randomly generated data and returns it along with its encoder
def train_dec_tree():
    
    # splits the data into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(input, output, test_size=0.25)

    # utilizes OneHotEncoder to convert categorical values
    onehot_encoder = OneHotEncoder(sparse=False, handle_unknown = 'ignore')
    encoded_train_X = onehot_encoder.fit_transform(X_train)

    # creates the decision tree classifier model and fits it to the converted training data
    dec_tree = xgb.XGBClassifier()
    dec_tree.fit(encoded_train_X, y_train)

    return [dec_tree, onehot_encoder]
