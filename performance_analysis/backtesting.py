import pandas as pd

class Backtester:
    def __init__(self, strategy, data):
        """
        Initialize the backtester with a trading strategy and historical data.

        :param strategy: A trading strategy function
        :param data: DataFrame with historical trading data
        """
        self.strategy = strategy
        self.data = data
        self.results = None

    def run_backtest(self):
        """
        Run the backtest using the specified strategy.

        :return: DataFrame with backtest results
        """
        self.results = self.strategy(self.data)
        return self.results

if __name__ == "__main__":
    # Load historical trading data (replace with your data source)
    trading_data = pd.read_csv('historical_trading_data.csv')

    # Define and import your trading strategy function (e.g., strategy1)
    from strategy1 import simple_moving_average_strategy

    # Initialize the backtester with the strategy and data
    backtester = Backtester(strategy=simple_moving_average_strategy, data=trading_data)

    # Run the backtest
    backtest_results = backtester.run_backtest()

    # Print or analyze the backtest results as needed
    print(backtest_results)
