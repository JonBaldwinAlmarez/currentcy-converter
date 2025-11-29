from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "fca_live_u71pCGI5QB9FGhyPWXAH8gmFOc1nGubZaLB8Pmbn"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"v1/latest?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()["data"]

    return data

def print_currencies(data):
    printer.pprint([f"{key}: {value}" for key, value in data.items()])

def exchange_rate():
    from_currency = input("Enter the currency you have (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want (e.g., EUR): ").upper()
    amount = float(input(f"Enter the amount of {from_currency} to convert: "))

    endpoint = f"v1/convert?apikey={API_KEY}&from={from_currency}&to={to_currency}&amount={amount}"
    url = BASE_URL + endpoint
    data = get(url).json()["data"]

    rate = data["rate"]
    converted_amount = data["result"]

    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency} at a rate of {rate}.")


#data = get_currencies()
#print_currencies(data)
    
exchange_rate()