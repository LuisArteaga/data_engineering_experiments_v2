# Connect to Azure Key Vault and retrieve the secret

# Connect to ebay and verify the credentials
import os
import requests


# Get the API key from the environment variables
APP_ID = os.environ.get('EBAY_DEVELOPER_APP_ID')
OAUTH_TOKEN = os.environ.get('EBAY_DEVELOPER_OAUTH_TOKEN')

# Test Ebay Browse API
URL = 'https://api.ebay.com/buy/browse/v1/item_summary/search'
QUERY = 'Art Of Problem Solving'

params = {
    'q': QUERY,
    'limit': 10,
    'offset': 0
    }

headers = {
    'X-EBAY-C-MARKETPLACE-ID': 'EBAY_DE',
    'X-EBAY-C-APP-ID': APP_ID,
    'Authorization': 'Bearer ' + OAUTH_TOKEN, 
    'Content-Type': 'application/json'
    }

response = requests.get(URL, params=params, headers=headers, timeout=200)
print(response.status_code)

print(response.text)



# Explore the API with math books as search term

