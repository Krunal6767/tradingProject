import pandas as pd

def execute_market_order(data, initial_cash, commission_fee):
    """
    Execute market orders in the trading data.

    :param data: DataFrame with trading data (including 'Signal' and 'Close' prices)
    :param initial_cash: Initial cash available for trading
    :param commission_fee: Commission fee per trade
    :return: Updated DataFrame with executed orders and cash balance
    """
    cash_balance = initial_cash
    data['Position_Size'] = 0  # Initialize position size column
    data['Cash_Balance'] = cash_balance  # Initialize cash balance column

    for i in range(len(data)):
        signal = data['Signal'].iloc[i]
        current_price = data['Close'].iloc[i]

        if signal == 1:  # Buy signal
            position_size = int(cash_balance / current_price)
            if position_size > 0:
                cash_balance -= position_size * current_price
                cash_balance -= commission_fee  # Deduct commission fee
                data.at[i, 'Position_Size'] = position_size

        elif signal == -1:  # Sell signal
            position_size = data['Position_Size'].iloc[i - 1]
            if position_size > 0:
                cash_balance += position_size * current_price
                cash_balance -= commission_fee  # Deduct commission fee
                data.at[i, 'Position_Size'] = 0

        # Update the cash balance in the DataFrame
        data.at[i, 'Cash_Balance'] = cash_balance

    return data

if __name__ == "__main__":
    # Load historical trading data with signals (replace with your data source)
    trading_data = pd.read_csv('historical_trading_data_with_signals.csv')

    # Specify initial cash and commission fee per trade
    initial_cash = 100000  # Replace with your initial cash balance
    commission_fee = 10  # Replace with your commission fee per trade

    # Execute market orders in the data
    updated_data = execute_market_order(trading_data, initial_cash, commission_fee)

    # Print the updated data with executed orders and cash balance
    print(updated_data)
