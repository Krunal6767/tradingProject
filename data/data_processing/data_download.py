import yfinance as yf

def download_stock_data(ticker, start_date, end_date, output_file):
    try:
        # Create a Yahoo Finance ticker object
        stock = yf.Ticker(ticker)

        # Download historical data
        data = stock.history(period="max", start=start_date, end=end_date)

        # Save the data to a CSV file
        data.to_csv(output_file)

        print(f"Data for {ticker} downloaded and saved to {output_file}")

    except Exception as e:
        print(f"Error downloading data: {e}")

if __name__ == "__main__":
    # Set your desired stock symbol, start date, end date, and output file name
    stock_ticker = "AAPL"  # Replace with the stock symbol you want
    start_date = "2020-01-01"
    end_date = "2023-01-01"
    output_file = "data/historical/stock_data.csv"  # Output file path

    download_stock_data(stock_ticker, start_date, end_date, output_file)
