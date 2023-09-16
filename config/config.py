import yaml

# Load the configuration from config.yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Access specific configuration parameters
strategy_name = config['strategy_name']
short_window = config['short_window']
long_window = config['long_window']
risk_percent = config['risk_percent']

# Print or use the loaded configuration as needed
print(f"Strategy Name: {strategy_name}")
print(f"Short Window: {short_window}")
print(f"Long Window: {long_window}")
print(f"Risk Percent: {risk_percent}")
