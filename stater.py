#!/usr/bin/env python3
import requests
import sys

if len(sys.argv) > 2:
    print("many arguments")
    sys.exit()

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

def main():
    sys.argv.pop(0)

    match sys.argv:
        case []:
            get_usd()
            get_eur()
            get_btc()
        case ['--all']:
            get_usd()
            get_eur()
            get_btc()
        case ['--usd']:
            get_usd()
        case ['--eur']:
            get_eur()
        case ['--btc']:
            get_btc()

main()