import requests
import matplotlib.pyplot as plt


# 1. GETTING  BITCOIN PRICE (INR + USD)

def get_bitcoin_price():
    url = "https://api.wazirx.com/api/v2/tickers/btcusdt"
    response = requests.get(url, timeout=20)
    data = response.json()
# Json we got from the api we use this could be changed as bitcoin price changes in every second 
    """{
  "ticker": {
    "last": "10352.21",
    "high": "10500",
    "low": "10050"
  }
}
"""
    price_usd = float(data["ticker"]["last"])        
    price_inr = price_usd * 83.20                    

    return price_usd, price_inr



# 2. CURRENCY CONVERTER

def convert_currency(btc, price_usd, price_inr, currency):

    if currency == "USD":
        return btc * price_usd
    elif currency == "INR":
        return btc * price_inr
    elif currency == "EUR":
        return btc * price_usd * 0.92
    elif currency == "GBP":
        return btc * price_usd * 0.79
    elif currency == "JPY":
        return btc * price_usd * 151.20
    else:
        return None



# 3. PRICE GRAPH (Last 50 trades)

def show_btc_graph():
    url = "https://api.wazirx.com/api/v2/trades?market=btcinr"
    response = requests.get(url, timeout=20)
    data = response.json()

    # Taking the last 50 prices
    prices = [float(item["price"]) for item in data][-50:]
    trades = list(range(len(prices)))

    plt.figure(figsize=(10,5))
    plt.plot(trades, prices, marker="o", linestyle="-")
    plt.title("Bitcoin Price Trend (INR) - Last 50 Trades")
    plt.xlabel("Trade Number")
    plt.ylabel("BTC Price (INR) ")
    plt.grid(True)
    plt.show()



# 4. MAIN CODE

print("<--BITCOIN PRICE TRACKER (WazirX API) -->")

try:
    price_usd, price_inr = get_bitcoin_price()

    print(f"Current BTC Price:")
    print(f"USD: ${price_usd:,.2f}")
    print(f"INR: ₹{price_inr:,.2f}")

    btc_amount = float(input("\nEnter Bitcoin amount: "))

    print("\nChoose Currency:")
    print("1. USD\n2. INR\n3. EUR\n4. GBP\n5. JPY")
    
    choice = int(input("Enter option number: "))

    currency_map = {1: "USD", 2: "INR", 3: "EUR", 4: "GBP", 5: "JPY"}
    currency = currency_map.get(choice)

    result = convert_currency(btc_amount, price_usd, price_inr, currency)

    if result is not None:
        print(f"\n{btc_amount} BTC = {result:,.2f} {currency}")
    else:
        print("Invalid currency choice.")

    print("\nGenerating BTC Price Graph…")
    show_btc_graph()

except Exception as e:
    print("Error occurred:", e)
