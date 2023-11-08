import requests
import sys
import json


def main():
    try:
        factor = float(sys.argv[1])
        call = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        cd_json = call.json()
        rate_str = cd_json["bpi"]["USD"]["rate"]
        rate = float(rate_str.replace(",", ""))
        bitcoin_v = factor * rate
        print(f"${bitcoin_v:,.4f}")
    except TypeError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")


main()