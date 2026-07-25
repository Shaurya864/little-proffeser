# Bitcoin Price Tracker & Currency Converter
A command-line Python tool that fetches the live Bitcoin price using the WazirX API, converts a given BTC amount into multiple currencies (USD, INR, EUR, GBP, JPY), and plots a price trend graph of the last 50 trades.

# Project Structure
bitcoin_tracker.py — Main script: fetches live price, converts currency, plots graph

requirements.txt — Python dependencies

README.md — This file


# Setup
python -m venv venv

venv\Scripts\activate      # Windows

pip install -r requirements.txt


# Usage
bash
python bitcoin_tracker.py


# The script will:

Fetch the current BTC price in USD (converted to INR using a fixed rate)
Ask you to enter a Bitcoin amount
Ask you to choose a currency to convert into (USD, INR, EUR, GBP, JPY)
Show the converted value
Plot a graph of BTC price movement over the last 50 trades (INR market)


# Example Output
<--BITCOIN PRICE TRACKER (WazirX API) -->
Current BTC Price:
USD: $67,245.30
INR: ₹55,95,010.96

Enter Bitcoin amount: 0.5

Choose Currency:
1. USD
2. INR
3. EUR
4. GBP
5. JPY
Enter option number: 2

0.5 BTC = 27,97,505.48 INR

Generating BTC Price Graph…

A matplotlib window will open showing the last 50 BTC/INR trades as a line graph.

# API Used
This project uses the WazirX API, specifically:

GET /api/v2/tickers/btcusdt — current BTC price in USD
GET /api/v2/trades?market=btcinr — recent BTC/INR trade history for the graph
USD → INR conversion uses a fixed rate (83.20) set in code, and EUR/GBP/JPY use fixed multipliers as well, rather than live rates.

# Note:
WazirX has scaled back trading operations after a security incident, so this API's uptime and data freshness are not guaranteed. If the API is unreachable, the script will print an error instead of crashing, thanks to the try/except block in main.

# Possible Extensions
Replace fixed currency conversion rates with a live forex API
Add error handling specifically for API downtime (retry logic)
Add more cryptocurrencies if the exchange supports them
Switch to a more actively maintained exchange API if WazirX becomes fully unavailable
Note
Bitcoin prices are highly volatile. This tool is for educational/tracking purposes only and should not be used as financial advice.

