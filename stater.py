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

def get_ars():
    r = requests.get("https://economia.awesomeapi.com.br/last/ARS-BRL")
    ars = r.json()['ARSBRL']['bid'] #peso argentino
    print(f"ARS = {ars}")

def get_jpy():
    r = requests.get("https://economia.awesomeapi.com.br/last/JPY-BRL")
    jpy = r.json()['JPYBRL']['bid']
    print(f"JPY = {jpy}")

def get_eth():
    r = requests.get("https://economia.awesomeapi.com.br/last/ETH-BRL")
    eth = r.json()['ETHBRL']['bid']
    print(f"ETH = {eth}")

def get_cny():
    r = requests.get("https://economia.awesomeapi.com.br/last/CNY-BRL")
    cny = r.json()['CNYBRL']['bid']
    print(f"CNY = {cny}")

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