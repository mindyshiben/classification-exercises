import pandas as pd
import os


def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    '''
    This function reads in titanic data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('titanic_df.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('titanic_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = new_titanic_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('titanic_df.csv')
        
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
        url = get_db_url('iris_db')
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
        url = get_db_url('telco_churn')
        df = pd.read_sql(query, url)
        df.to_csv(filename)

        return df  
