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



data = get_currencies()
printer.pprint(data)