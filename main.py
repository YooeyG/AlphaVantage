# main.py
import requests

from config import API_KEY

print(API_KEY)


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=' + API_KEY
r = requests.get(url)
data = r.json()

print(data)