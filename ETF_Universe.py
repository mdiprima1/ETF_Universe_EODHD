import requests

# Use your actual API token here
api_token = 'YOUR FREE API TOKEN HERE'

# Use the correct exchange code for US ETFs
EXCHANGE_CODE = 'US'
url = f'https://eodhd.com/api/exchange-symbol-list/{EXCHANGE_CODE}?api_token={api_token}&fmt=json&type=etf'

try:
    response = requests.get(url)
    response.raise_for_status()  # This will raise an exception for HTTP error codes
    data = response.json()  # Convert response to JSON

    # Only list CODE and NAME
    for etf in data:
        code = etf.get('Code')  # Adjust the key if necessary
        name = etf.get('Name')  # Adjust the key if necessary
        print(f'Code: {code}, Name: {name}')

    # Print total number of ETFs found
    print(f'{len(data)} ETFs found')

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except requests.exceptions.RequestException as err:
    print(f'Other error occurred: {err}')
except Exception as e:
    print(f'An error occurred: {e}')
