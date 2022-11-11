import pandas as pd
from matrix_factorization import KernelMF, train_update_test_split

data = pd.read_csv('random_data.csv')
# X is all columns except attend, y is attend
X = data.drop(['ATTEND?'], axis='columns')
y = data['ATTEND?']

def train_matrix_factorization():
    # split the data
    (
    X_train_initial, 
    y_train_initial,
    X_train_update,
    y_train_update, 
    X_test, 
    y_test
    )= train_update_test_split(data, frac_new_users=0.2)

    # initial training
    m_fact = KernelMF(n_epochs=20, n_factors=100, verbose=1, lr=0.001, reg=0.005)
    m_fact.fit(X_train_initial, y_train_initial)

    # update model
    m_fact.update_users(X_train_update, y_train_update, lr=0.001, n_epochs=20, verbose=1)
    return m_fact
