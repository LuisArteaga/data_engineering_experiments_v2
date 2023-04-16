# Connect to Azure Key Vault and retrieve the secret

# Connect to ebay and verify the credentials
import os
import requests


# Get the API key from the environment variables
API_KEY = os.environ.get('API_KEY')
APP_ID = os.environ.get('APP_ID')

# Test Ebay Browse API
URL = 'https://api.ebay.com/buy/browse/v1/item_summary/search'

params = {
    'q': 'math books',
    'limit': 10,
    'offset': 0
    }

headers = {
    'X-EBAY-C-MARKETPLACE-ID': 'EBAY_DE',
    'X-EBAY-C-APP-ID': APP_ID,
    #'X-EBAY-API-IAF-TOKEN' : API_KEY,
    'Authorization': 'Bearer ' + API_KEY, 
    'Content-Type': 'application/json'
    }

response = requests.get(URL, params=params, headers=headers)
print(response.status_code)

print(response.text)
print(response.json())
print(response.headers)


# Explore the API with math books as search term

