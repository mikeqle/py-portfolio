import pandas as pd
import requests
import os
from tabulate import tabulate
from apikey import ALPHA_VANTAGE_API_KEY
from helpers import get_price, clear_screen

# Replace YOUR_API_KEY with your Alpha Vantage API key
portfolio = pd.read_csv('/Users/mike/git-projects/2023/python-portfolio-tracker/portfolio.csv', index_col='ID')

# Add a new column for the stock price
portfolio['Price'] = None

# Get the stock price for each ticker in the portfolio
for i, row in portfolio.iterrows():
    ticker = row['Ticker']
    portfolio.loc[i, 'Price'] = get_price(ticker)

# Calculate the total value of each stock holding and the portfolio as a whole
portfolio['Total Value'] = portfolio['Shares'] * portfolio['Price']
total_value = portfolio['Total Value'].sum()

# Calculate the % Portfolio for each row
portfolio['% Portfolio'] = portfolio['Total Value'] / total_value

# Format the Total Value and % Portfolio columns
portfolio['Total Value'] = portfolio['Total Value'].apply(lambda x: f'${x:.2f}')

# Sort the portfolio by % Portfolio in descending order
portfolio = portfolio.sort_values(by='% Portfolio', ascending=False)
portfolio['% Portfolio'] = portfolio['% Portfolio'].apply(lambda x: f'{x:.2%}')

# Output the portfolio in the terminal
clear_screen()
print('Portfolio:')
print()
print(tabulate(portfolio, headers='keys', tablefmt='psql', showindex=True))
print()
print(f'Total Portfolio Value: ${total_value:.2f}')