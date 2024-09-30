import requests
import sys

def main():
    if len(sys.argv) == 2:
        try:
            value= float(sys.argv[1])
        except ValueError:
            print("Missing command-line argument")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        request_function= requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        convert_function= request_function.json()
        bitcoin_price=convert_function["bpi"]["USD"]["rate_float"]
        bitcoin_convert= bitcoin_price * value
        print(f"${bitcoin_convert:,.4f}")
    except requests.RequestException:
        print("request exception")
        sys.exit(1)

main()
