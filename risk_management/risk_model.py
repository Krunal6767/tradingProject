import pandas as pd
import numpy as np

def calculate_portfolio_volatility(returns):
    """
    Calculate the portfolio volatility.

    :param returns: DataFrame with asset returns
    :return: Portfolio volatility (standard deviation)
    """
    cov_matrix = returns.cov()
    weights = np.ones(len(returns.columns)) / len(returns.columns)
    portfolio_var = np.dot(weights.T, np.dot(cov_matrix, weights))
    portfolio_volatility = np.sqrt(portfolio_var)
    return portfolio_volatility

def calculate_portfolio_var(returns, alpha=0.05):
    """
    Calculate the Value at Risk (VaR) of the portfolio.

    :param returns: DataFrame with asset returns
    :param alpha: Confidence level for VaR calculation
    :return: Portfolio VaR
    """
    portfolio_volatility = calculate_portfolio_volatility(returns)
    z_score = -1.645  # Z-score for a 5% confidence level (adjust as needed)
    portfolio_var = portfolio_volatility * z_score
    return portfolio_var

if __name__ == "__main__":
    # Load portfolio returns (replace with your data source)
    returns_data = pd.read_csv('portfolio_returns.csv')

    # Calculate portfolio volatility
    portfolio_volatility = calculate_portfolio_volatility(returns_data)
    print(f"Portfolio Volatility: {portfolio_volatility:.4f}")

    # Calculate portfolio VaR at a 5% confidence level
    portfolio_var = calculate_portfolio_var(returns_data, alpha=0.05)
    print(f"Portfolio VaR (5% confidence level): {portfolio_var:.4f}")
