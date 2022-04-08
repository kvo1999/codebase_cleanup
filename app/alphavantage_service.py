
import os
from dotenv import load_dotenv
import requests
import json
from pandas import read_csv

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def fetch_crypto_data(symbol):
    """
    this function allows us to import the crypto data of our choosing
    invoke like: fetch_crypto_data(symbol)
    returns: crypto data for later exploration
    """
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    return parsed_response




def fetch_stocks_data(symbol):
    """
    this function allows us to import the stocks data of our choosing
    invoke like: fetch_stocks_data(symbol)
    returns: stock data for later exploration
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    df = read_csv(url)
    return df


def fetch_unemployment_data():
    """
    this function allows us to import the unemployment data 
    invoke like: fetch_unemployment_data()
    returns: unemployment data for later exploration
    """
    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    return parsed_response 

