import numpy as np
import pandas as pd

def missing_count(col):
    return col.isnull().sum()


def data_overview(data, message):
    print(message)
    print("\n")

    # No of rows & columns
    print(f"Entries in the dataset: {data.shape[0]}")
    print(f"Features in the dataset: {data.shape[1]}")
    print("\n")

    # Features
    print(f"Faatures of the dataset:\n {list(data.columns)}")
    print("\n")
    
    # Count of missing values in each feature
    print("Missing Values:")
    for feature in data.columns:
        count = missing_count(data[feature])
        print(f"{feature:30s}: {count}")
    print("\n")
    
    # Unqiue values in each feature
    print("Unqiue Values:")
    for feature in data.columns:
        print(f"{feature:30s}: {data[feature].nunique()}")
    print("\n")
    
    # Features of string dtype
    print("String type features: ")
    for feature in data.columns:
        if(isinstance(data[feature][0], str)):
            print(feature)
    print("\n")
    
    # Feature of numerical dtype
    print("Numerical type features: ")
    for feature in data.columns:
        if(isinstance(data[feature][0], np.int32) or isinstance(data[feature][0], np.int64) or isinstance(data[feature][0], float)):
            print(feature)
    print("\n")