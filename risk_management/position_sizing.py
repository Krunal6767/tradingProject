import pandas as pd

def position_size_equity_percent(equity, risk_percent):
    """
    Calculate position size as a percentage of total equity.

    :param equity: Total equity available for trading
    :param risk_percent: Maximum percentage of equity to risk on a single trade
    :return: Position size
    """
    position_size = (equity * risk_percent) / 100.0
    return position_size

def position_size_fixed_quantity(fixed_quantity):
    """
    Calculate position size as a fixed quantity.

    :param fixed_quantity: Fixed quantity of shares/contracts to trade
    :return: Position size
    """
    return fixed_quantity

if __name__ == "__main__":
    # Total equity available for trading
    total_equity = 100000  # Replace with your total equity

    # Maximum risk as a percentage of equity
    risk_percent = 2.0  # Replace with your risk tolerance

    # Calculate position size based on equity percentage
    equity_percent_position_size = position_size_equity_percent(total_equity, risk_percent)
    print(f"Position Size (Equity Percent): {equity_percent_position_size:.2f} shares/contracts")

    # Calculate position size based on a fixed quantity
    fixed_quantity_position_size = position_size_fixed_quantity(100)  # Replace with your desired fixed quantity
    print(f"Position Size (Fixed Quantity): {fixed_quantity_position_size} shares/contracts")
