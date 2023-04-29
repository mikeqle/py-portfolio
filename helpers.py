import os
import requests
from bs4 import BeautifulSoup

# Replace YOUR_API_KEY with your Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_price(ticker):
    print(f'Fetching {ticker}...')
    url = f'https://www.google.com/finance/quote/{ticker}'
    response = requests.get(url)

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div element with the classes "YMlKec" and "fxKbKc"
    price_div = soup.find('div', {'class': 'YMlKec fxKbKc'})

    # Extract the text content of the div and convert it to a float
    if (price_div is None):
        price = 0
    else:
        price = float(price_div.text[1:])

    return price
