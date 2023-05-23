import os
import requests
from bs4 import BeautifulSoup
from env_variables import COOKIES_CONSENT, COOKIES_SOC, COOKIES_OTZ, COOKIES_ENID

# Replace YOUR_API_KEY with your Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_price(ticker):
    url = f'https://www.google.com/finance/quote/{ticker}'

    # Set cookies
    cookies = {
        'CONSENT': COOKIES_CONSENT,
        'SOCS': COOKIES_SOC,
        'OTZ': COOKIES_OTZ,
        '__Secure-ENID': COOKIES_ENID
    }

    response = requests.get(url, cookies=cookies)
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the div element with the classes "YMlKec" and "fxKbKc"
    price_div = soup.find('div', {'class': 'YMlKec fxKbKc'})

    # Extract the text content of the div and convert it to a float
    if (price_div is None):
        price = 0
    else:
        price = float(price_div.text[1:])
    print(f'Fetched {ticker}: {price}')

    return price
