import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

def read_data():
    cwd = os.getcwd()
    data_path = os.path.join(cwd, 'dataset/train.csv')
    data = pd.read_csv(data_path)
    return data

def preprocess(df):
    numeric=df.select_dtypes(include=['float64','int64'])
    correlation_threshold = 0.2  
    low_corr_columns = numeric.columns[(abs(numeric.corr()['SalePrice']) < correlation_threshold)]
    numeric_filtered = numeric.drop(columns=low_corr_columns)
    numeric_filled=numeric_filtered.fillna(0)
    return numeric_filled

def get_xy(data):
    X = data.drop(columns=['SalePrice'])
    y = data['SalePrice']
    return X, y

def pipeline():
    data = read_data()
    data_proc = preprocess(data)
    X, y = get_xy(data_proc)
    return X,y