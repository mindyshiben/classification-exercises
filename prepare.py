import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

import acquire

def prep_iris(df):
    df = df.drop(['measurement_id', 'species_id'], axis=1)
    df.rename(columns = {'species_name':'species'}, inplace =True)
    dummy_df = pd.get_dummies(df[['species']], dummy_na=False, drop_first=[True])
    df = pd.concat([df, dummy_df], axis=1)
    return df 

def prep_titanic(df):
    df = df.drop(['Unnamed: 0', 'passenger_id','pclass', 'deck', 'embarked'], axis=1)
    dummy_df = pd.get_dummies(df[['sex', 'embark_town', 'class']], dummy_na=False, drop_first=[True, True, True])
    df = pd.concat([dummy_df, df], axis=1)
    return df

def prep_telco(df):
    df = df.drop(['Unnamed: 0', 'customer_id'], axis=1)
    dummy = pd.get_dummies(df[['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines',
                  'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing',
                  'churn', 'internet_service_type', 'payment_type', 'contract_type']],
              dummy_na=False, drop_first=[True, True, True, True, True, True, True, True, True, True, True, True, True])
    df = pd.concat([dummy, df], axis=1)
    return df
    