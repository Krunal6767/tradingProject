import pandas as pd

def calculate_performance_metrics(data, risk_free_rate):
    """
    Calculate performance metrics for a trading strategy.

    :param data: DataFrame with trading data (including 'Position_Size' and 'Returns')
    :param risk_free_rate: Annual risk-free rate for benchmarking (e.g., 0.02 for 2%)
    :return: Dictionary of performance metrics
    """
    metrics = {}

    # Total Returns
    total_returns = (data['Position_Size'] * data['Returns']).sum()
    metrics['Total_Returns'] = total_returns

    # Annualized Returns
    annualized_returns = ((1 + total_returns) ** (252 / len(data))) - 1
    metrics['Annualized_Returns'] = annualized_returns

    # Volatility (annualized)
    volatility = data['Returns'].std() * (252 ** 0.5)
    metrics['Volatility'] = volatility

    # Sharpe Ratio
    sharpe_ratio = (annualized_returns - risk_free_rate) / volatility
    metrics['Sharpe_Ratio'] = sharpe_ratio

    # Maximum Drawdown
    max_drawdown = calculate_max_drawdown(data)
    metrics['Max_Drawdown'] = max_drawdown

    return metrics

def calculate_max_drawdown(data):
    """
    Calculate the maximum drawdown of a trading strategy.

    :param data: DataFrame with trading data (including 'Position_Size' and 'Returns')
    :return: Maximum drawdown as a percentage
    """
    cum_returns = (data['Position_Size'] * data['Returns'] + 1).cumprod()
    peak = cum_returns.cummax()
    drawdown = (cum_returns / peak - 1) * 100
    max_drawdown = drawdown.min()
    return max_drawdown

if __name__ == "__main__":
    # Load trading data with positions and returns (replace with your data source)
    trading_data = pd.read_csv('historical_trading_data_with_returns.csv')

    # Specify the risk-free rate for benchmarking (e.g., 0.02 for 2%)
    risk_free_rate = 0.02

    # Calculate performance metrics
    metrics = calculate_performance_metrics(trading_data, risk_free_rate)

    # Print the calculated metrics
    print("Performance Metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")
