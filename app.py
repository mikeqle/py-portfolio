import pandas as pd
import requests
import os
from tabulate import tabulate
# Replace YOUR_API_KEY with your Alpha Vantage API key
API_KEY = os.environ['ALPHA_VANTAGE_API_KEY']

# Read in the portfolio CSV file using pandas
portfolio = pd.read_csv('portfolio.csv', index_col='ID')

# Add a new column for the stock price
portfolio['Price'] = None

# Helper funcs
def clear_screen():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS and Linux
        os.system("clear")

# Get the stock price for each ticker in the portfolio
for i, row in portfolio.iterrows():
    ticker = row['Ticker']
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    if 'Global Quote' in data:
        price = float(data['Global Quote']['05. price'])
        portfolio.loc[i, 'Price'] = price
    else:
        print(f'Error: Unable to retrieve stock price for {ticker}.')

# Calculate the total value of each stock holding and the portfolio as a whole
portfolio['Total Value'] = portfolio['Shares'] * portfolio['Price']
total_value = portfolio['Total Value'].sum()


# Output the portfolio in the terminal
clear_screen()
print("Portfolio")
print(tabulate(portfolio, headers = 'keys', tablefmt = 'psql'))
print(f'Total Portfolio Value: ${total_value:.2f}')
