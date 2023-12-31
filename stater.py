#!/usr/bin/env python3
import requests
import sys
from rainbowio import *

if len(sys.argv) > 2:
    print_rgb("red", "many arguments")
    sys.exit()

def get_value(coin: str):
    try:
        coin = coin.upper()
        url = f"https://economia.awesomeapi.com.br/last/{coin}-BRL"
        r = requests.get(url)
        value = r.json()[f'{coin}BRL']['bid']
        print_rgb("green", f"{coin} = {value}")
    except:
        print_rgb("red", "error")

def get_all():
    get_value("usd")
    get_value("eur")
    get_value("btc")
    get_value("ars")
    get_value("jpy")
    get_value("eth")
    get_value("cny")

def main():
    sys.argv.pop(0)

    match sys.argv:
        case []:
            get_all()
        case ['--all']:
            get_all()
        case ['--usd']:
            get_value("usd")
        case ['--eur']:
            get_value("eur")
        case ['--btc']:
            get_value("btc")
        case ['--ars']:
            get_value("ars")
        case ['--jpy']:
            get_value("jpy")
        case ['--eth']:
            get_value("eth")
        case ['--cny']:
            get_value("cny")
        case _:
            print("invalid command")

main()