import pandas as pd

def simple_moving_average_strategy(data, short_window, long_window):
    # Calculate short-term and long-term moving averages
    data['SMA_Short'] = data['Close'].rolling(window=short_window).mean()
    data['SMA_Long'] = data['Close'].rolling(window=long_window).mean()

    # Initialize trading signals
    data['Signal'] = 0  # 0 indicates no action

    # Generate buy (1) and sell (-1) signals based on crossover
    data.loc[data['SMA_Short'] > data['SMA_Long'], 'Signal'] = 1
    data.loc[data['SMA_Short'] < data['SMA_Long'], 'Signal'] = -1

    return data

if __name__ == "__main__":
    # Load preprocessed historical stock price data
    input_file = "data/historical/preprocessed_stock_data.csv"
    stock_data = pd.read_csv(input_file)

    # Define the short-term and long-term moving average windows
    short_window = 50
    long_window = 200

    # Apply the SMA crossover strategy
    stock_data = simple_moving_average_strategy(stock_data, short_window, long_window)

    # Print the updated data with trading signals
    print(stock_data)
