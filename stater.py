#!/usr/bin/env python3
import requests
import sys

if len(sys.argv) > 2:
    print("many arguments")
    sys.exit()

def get_usd(): #Dólar Americano
    try:
        r = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        usd = r.json()['USDBRL']['bid']
        print(f"USD = {usd}")
    except:
        print("error")

def get_eur(): #Euro
    try:
        r = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
        eur = r.json()['EURBRL']['bid']
        print(f"EUR = {eur}")
    except:
        print("error")

def get_btc(): #Bitcoin
    try:
        r = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
        btc = r.json()['BTCBRL']['bid']
        print(f"BTC = {btc}")
    except:
        print("error")

def get_ars(): #Peso Argentino
    try:
        r = requests.get("https://economia.awesomeapi.com.br/last/ARS-BRL")
        ars = r.json()['ARSBRL']['bid'] #peso argentino
        print(f"ARS = {ars}")
    except:
        print("error")

def get_jpy(): #Iene Japonês
    try:
        r = requests.get("https://economia.awesomeapi.com.br/last/JPY-BRL")
        jpy = r.json()['JPYBRL']['bid']
        print(f"JPY = {jpy}")
    except:
        print("error")

def get_eth(): #Ethereum
    try:
        r = requests.get("https://economia.awesomeapi.com.br/last/ETH-BRL")
        eth = r.json()['ETHBRL']['bid']
        print(f"ETH = {eth}")
    except:
        print("error")

def get_cny(): #Yuan Chinês
    try:
        r = requests.get("https://economia.awesomeapi.com.br/last/CNY-BRL")
        cny = r.json()['CNYBRL']['bid']
        print(f"CNY = {cny}")
    except:
        print("error")

def get_all():
    get_usd()
    get_eur()
    get_btc()
    get_ars()
    get_jpy()
    get_eth()
    get_cny()

def main():
    sys.argv.pop(0)

    match sys.argv:
        case []:
            get_all()
        case ['--all']:
            get_all()
        case ['--usd']:
            get_usd()
        case ['--eur']:
            get_eur()
        case ['--btc']:
            get_btc()
        case ['--ars']:
            get_ars()
        case ['--jpy']:
            get_jpy()
        case ['--eth']:
            get_eth()
        case ['--cny']:
            get_cny()
        case _:
            print("invalid command")

main()