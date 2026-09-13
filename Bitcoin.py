
import sys
import requests
def main():
    if len(sys.argv!=2):
        sys.exit("Usage :python bitcoin.py <number_of_bit coins>")

    try:
        n=float(sys.argv[1])
    except ValueError:
        sys.exit("Error :Argument must be number")

    api_key="YourApiKeyHere"
    url=f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey"
    try:
        response=requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("error : unable to fetch data")
    try:
        data=response.json()
        price=float(data["data"]["priceUsd"])

    except (KeyError, ValueError, TypeError):
        sys.exit("Error : Unexpected API response format")

    cost = n * price
    print(f"${cost:,.4f}")
if __name__=="__main__":
    main()