import requests
import pandas as pd
import openpyxl
import schedule
import time

# API URL to fetch live cryptocurrency data
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": False
}

# Excel file path
EXCEL_FILE = "crypto_data.xlsx"

def fetch_crypto_data():
    """Fetches the top 50 cryptocurrencies by market cap from CoinGecko API."""
    response = requests.get(API_URL, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return []

def analyze_data(data):
    """Performs basic analysis on the fetched cryptocurrency data."""
    df = pd.DataFrame(data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"])
    
    # Top 5 cryptocurrencies by market cap
    top_5 = df.nlargest(5, "market_cap")

    # Average price of top 50 cryptocurrencies
    avg_price = df["current_price"].mean()

    # Highest & lowest 24-hour percentage price change
    highest_24h = df.loc[df["price_change_percentage_24h"].idxmax()]
    lowest_24h = df.loc[df["price_change_percentage_24h"].idxmin()]

    # Display analysis
    print("\n🔹 Top 5 Cryptocurrencies by Market Cap:")
    print(top_5[["name", "market_cap"]])
    print(f"\n🔹 Average Price of Top 50: ${avg_price:.2f}")
    print(f"\n🔹 Highest 24h Price Change: {highest_24h['name']} ({highest_24h['price_change_percentage_24h']}%)")
    print(f"🔹 Lowest 24h Price Change: {lowest_24h['name']} ({lowest_24h['price_change_percentage_24h']}%)\n")

    return df, top_5, avg_price, highest_24h, lowest_24h

def update_excel(data):
    """Updates the Excel file with live cryptocurrency data."""
    df = pd.DataFrame(data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"])
    
    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="w") as writer:
        df.to_excel(writer, sheet_name="Live Data", index=False)

    print(f"✅ Excel updated: {EXCEL_FILE}")

def main():
    """Main function to fetch, analyze, and update Excel."""
    print("\n🔄 Fetching cryptocurrency data...")
    data = fetch_crypto_data()

    if data:
        df, top_5, avg_price, highest_24h, lowest_24h = analyze_data(data)
        update_excel(data)

# Schedule the script to run every 5 minutes
schedule.every(5).minutes.do(main)

print("\n📊 Crypto Data Tracker is running... (Press Ctrl+C to stop)")
main()  # Run first time immediately

while True:
    schedule.run_pending()
    time.sleep(1)
