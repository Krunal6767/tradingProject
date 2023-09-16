import pandas as pd

def momentum_strategy(data, roc_period, threshold):
    # Calculate the Rate of Change (ROC) indicator
    data['ROC'] = data['Close'].pct_change(roc_period) * 100

    # Initialize trading signals
    data['Signal'] = 0  # 0 indicates no action

    # Generate buy (1) and sell (-1) signals based on ROC
    data.loc[data['ROC'] > threshold, 'Signal'] = 1
    data.loc[data['ROC'] < -threshold, 'Signal'] = -1

    return data

if __name__ == "__main__":
    # Load historical stock price data (replace with your data source)
    data = pd.read_csv('historical_stock_data.csv')

    # Define ROC period and threshold
    roc_period = 14  # Adjust as needed
    threshold = 2.0  # Adjust as needed

    # Apply the momentum-based strategy
    data = momentum_strategy(data, roc_period, threshold)

    # Print the data with trading signals
    print(data)
