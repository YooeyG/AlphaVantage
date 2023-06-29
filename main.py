# main.py
import requests
import pandas as pd
from config import API_KEY

print(API_KEY)


Ticker = 'IBM'

#INCOME STATEMENT
base_url = 'https://www.alphavantage.co/query?'
params_IS = {'function': 'INCOME_STATEMENT',
         'symbol': Ticker,
         'apikey': API_KEY}

IS = requests.get(base_url, params=params_IS).json()


#BALANCE SHEET
params_BS = {'function': 'BALANCE_SHEET',
         'symbol': Ticker,
         'apikey': API_KEY}

BS = requests.get(base_url, params=params_BS).json()

#CASH FLOW
params_CF = {'function': 'CASH_FLOW',
         'symbol': Ticker,
         'apikey': API_KEY}

CF = requests.get(base_url, params=params_BS).json()




# Determine the type of data
data_type = type(IS)
print(data_type)


#RECURSSION
def flatten_json(nested_json):
    """
        Flatten json object with nested keys into a single level.
            Args: nested_json: A nested json object.
            Returns: The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

IS_df = pd.Series(flatten_json(IS)).to_frame()
print(IS_df)

BS_df = pd.Series(flatten_json(BS)).to_frame()
print(BS_df)

CF_df = pd.Series(flatten_json(CF)).to_frame()
print(CF_df)

#PUT EACH INTO AN EXCEL FILE
CF_df.to_excel('output_CF.xlsx', index=False)
BS_df.to_excel('output_BS.xlsx', index=False)
IS_df.to_excel('output_IS.xlsx', index=False)