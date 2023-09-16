import yaml

# Load the secret configuration from secret.yaml
with open('secret.yaml', 'r') as secret_file:
    secrets = yaml.safe_load(secret_file)

# Access specific secret values
api_key = secrets['api_key']
api_secret = secrets['api_secret']
username = secrets['username']
password = secrets['password']

# Use the loaded secrets as needed
print(f"API Key: {api_key}")
print(f"API Secret: {api_secret}")
print(f"Username: {username}")
print(f"Password: {password}")
