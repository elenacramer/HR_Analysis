import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def split(df, test_size):
    X = df.drop("target", axis=1)
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test

def normalize_data(X_train, X_test):
    norm = MinMaxScaler().fit(X_train)
    names = X_train.columns
    X_train_norm = norm.transform(X_train)
    X_test_norm = norm.transform(X_test)
    return pd.DataFrame(X_train_norm, columns=[names]), pd.DataFrame(X_test_norm, columns=[names])