#!/usr/bin/env python3
import requests
import sys
from rainbowio import *

if len(sys.argv) > 2:
    print_rgb("red", "many arguments")
    sys.exit()

def get_value(coin: str, color: str):
    try:
        coin = coin.upper()
        url = f"https://economia.awesomeapi.com.br/last/{coin}-BRL"
        r = requests.get(url)
        value = r.json()[f'{coin}BRL']['bid']
        print_rgb(color, f"{coin} = {value}")
    except:
        print_rgb("red", "error")

def get_all():
    get_value("usd", "green")
    get_value("eur", "blue")
    get_value("btc", "yellow")
    get_value("ars", "blue")
    get_value("jpy", "magenta")
    get_value("eth", "blue")
    get_value("cny", "red")

def main():
    sys.argv.pop(0)

    match sys.argv:
        case []:
            get_all()
        case ['--all']:
            get_all()
        case ['--usd']:
            get_value("usd", "green")
        case ['--eur']:
            get_value("eur", "blue")
        case ['--btc']:
            get_value("btc", "yellow")
        case ['--ars']:
            get_value("ars", "blue")
        case ['--jpy']:
            get_value("jpy", "magenta")
        case ['--eth']:
            get_value("eth", "blue")
        case ['--cny']:
            get_value("cny", "red")
        case _:
            print("invalid command")

main()