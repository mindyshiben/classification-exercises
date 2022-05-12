import pandas as pd
import os
from env import get_db_url

def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''
        SELECT *
        FROM passengers;        
        '''
        url = env.get_db_url('titanic_db')
        df = pd.read_sql(query, url)
        df.to_csv(filename)

        return df  

def get_iris_data():
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''
        SELECT *
        FROM measurements
        JOIN
        species USING(species_id);      
        '''
        url = env.get_db_url('iris_db')
        df = pd.read_sql(query, url)
        df.to_csv(filename)

        return df  

def get_telco_data():
    filename = "telco.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''
        SELECT * 
        FROM customers
        JOIN contract_types USING (contract_type_id)
        JOIN payment_types USING (payment_type_id)
        JOIN internet_service_types USING (internet_service_type_id)
        JOIN customer_payments USING(customer_id) ;     
        '''
        url = env.get_db_url('telco_churn')
        df = pd.read_sql(query, url)
        df.to_csv(filename)

        return df  
