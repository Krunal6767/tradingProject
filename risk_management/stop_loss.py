import pandas as pd

def apply_stop_loss(data, stop_loss_percent):
    """
    Apply a simple percentage-based stop-loss to the trading data.

    :param data: DataFrame with trading data (including 'Close' prices)
    :param stop_loss_percent: Percentage at which to trigger the stop-loss
    :return: Updated DataFrame with stop-loss orders
    """
    data['Stop_Loss'] = 0.0  # Initialize stop-loss column

    for i in range(1, len(data)):
        current_price = data['Close'].iloc[i]
        previous_price = data['Close'].iloc[i - 1]

        # Calculate the stop-loss level based on the previous close
        stop_loss_level = previous_price * (1 - stop_loss_percent / 100)

        # Set the stop-loss level in the 'Stop_Loss' column
        data.at[i, 'Stop_Loss'] = stop_loss_level

        # Check if the current price has reached or breached the stop-loss level
        if current_price <= stop_loss_level:
            # Implement the stop-loss by selling the position (you can modify this logic)
            data.at[i, 'Stop_Loss_Order'] = 'SELL'
            data.at[i, 'Position_Size'] = 0  # Reset position size

    return data

if __name__ == "__main__":
    # Load historical trading data (replace with your data source)
    trading_data = pd.read_csv('historical_trading_data.csv')

    # Specify the stop-loss percentage (e.g., 5%)
    stop_loss_percent = 5.0

    # Apply the stop-loss mechanism to the data
    updated_data = apply_stop_loss(trading_data, stop_loss_percent)

    # Print the updated data with stop-loss orders
    print(updated_data)
