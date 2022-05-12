import pandas as pd
import numpy as np
import os
from env import get_db_url


def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql('SELECT * FROM passengers', get_db_url('titanic_db'))
        df.to_csv(filename)
        return df  

def get_iris_data():
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        sql = """
        SELECT *
        FROM measurements
        JOIN species USING(species_id)
        """
        df = pd.read_sql(sql, get_db_url('iris_db'))
        df.to_csv(filename)

        return df 

def get_telco_data():
    filename = "telco.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        sql = """
        SELECT *
        FROM customers
        JOIN internet_service_types USING(internet_service_type_id)
        JOIN payment_types USING(payment_type_id)
        JOIN contract_types USING(contract_type_id)
        """
        df = pd.read_sql(sql, get_db_url('telco_churn'))
        df.to_csv(filename)

        return df 