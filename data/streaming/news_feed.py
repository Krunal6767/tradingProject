import requests
import json
import time

# Replace 'YOUR_API_KEY' with your actual News API key
NEWS_API_KEY = 'YOUR_API_KEY'

# Function to fetch and display news articles
def fetch_news_articles(api_key, query):
    while True:
        try:
            # Define the News API URL
            url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'

            # Send a GET request to the API
            response = requests.get(url)

            # Parse the JSON response
            data = response.json()

            # Check if the request was successful
            if data['status'] == 'ok':
                articles = data['articles']

                # Display the latest news headlines
                for i, article in enumerate(articles):
                    print(f"{i + 1}. {article['title']}")
                    print(article['description'])
                    print(article['url'])
                    print("\n")

        except Exception as e:
            print(f"Error fetching news data: {e}")

        # Fetch news data at regular intervals (e.g., every 30 seconds)
        time.sleep(30)

if __name__ == "__main__":
    search_query = "stock market"  # Change this to your desired search query
    fetch_news_articles(NEWS_API_KEY, search_query)
