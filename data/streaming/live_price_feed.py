import yfinance as yf
import time


def get_live_stock_price(ticker):
    """

    :param ticker:
    """
    while True:
        try:
            # Create a Yahoo Finance ticker object
            stock = yf.Ticker(ticker)

            # Get the most recent data
            data = stock.history(period="1d")

            # Extract the latest closing price
            latest_price = data["Close"].iloc[-1]

            print(f"Live {ticker} Price: ${latest_price:.2f}")

        except Exception as e:
            print(f"Error fetching data: {e}")

        # Fetch data at regular intervals (e.g., every 10 seconds)
        time.sleep(10)


if __name__ == "__main__":
    stock_ticker = "AAPL"  # Change this to the stock you want to monitor
    get_live_stock_price(stock_ticker)
