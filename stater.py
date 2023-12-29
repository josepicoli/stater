import requests
import sys

def get_usd():
    r = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    usd = r.json()['USDBRL']['bid']
    print(f"USD = {usd}")

def get_eur():
    r = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
    eur = r.json()['EURBRL']['bid']
    print(f"EUR = {eur}")

def get_btc():
    r = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
    btc = r.json()['BTCBRL']['bid']
    print(f"BTC = {btc}")

get_usd()
get_eur()
get_btc()