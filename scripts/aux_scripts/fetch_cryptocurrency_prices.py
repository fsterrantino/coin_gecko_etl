import requests

def fetch_cryptocurrency_prices(api_url, headers):
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            '''
            for crypto in data:
                print(f"{crypto['name']}: {crypto['price']} {crypto['symbol']}")
            '''
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error: {e}")