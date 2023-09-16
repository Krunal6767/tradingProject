import pandas as pd

def mean_reversion_strategy(data, lookback_period, z_score_threshold):
    # Calculate the moving average
    data['SMA'] = data['Close'].rolling(window=lookback_period).mean()

    # Calculate the standard deviation
    data['StdDev'] = data['Close'].rolling(window=lookback_period).std()

    # Calculate the Z-score
    data['Z_Score'] = (data['Close'] - data['SMA']) / data['StdDev']

    # Initialize trading signals
    data['Signal'] = 0  # 0 indicates no action

    # Generate buy (1) and sell (-1) signals based on Z-score
    data.loc[data['Z_Score'] > z_score_threshold, 'Signal'] = -1
    data.loc[data['Z_Score'] < -z_score_threshold, 'Signal'] = 1

    return data

if __name__ == "__main__":
    # Load historical stock price data (replace with your data source)
    data = pd.read_csv('historical_stock_data.csv')

    # Define lookback period and Z-score threshold
    lookback_period = 20
    z_score_threshold = 1.0

    # Apply the mean reversion strategy
    data = mean_reversion_strategy(data, lookback_period, z_score_threshold)

    # Print the data with trading signals
    print(data)
