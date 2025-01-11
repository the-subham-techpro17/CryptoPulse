import requests

def get_crypto_price():
    # Replace with the correct API URL for real-time crypto prices
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,inr"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Extract the prices for USD and INR
        prices = {
            'bitcoin': {
                'usd': data['bitcoin']['usd'],
                'inr': data['bitcoin']['inr']
            },
            'ethereum': {
                'usd': data['ethereum']['usd'],
                'inr': data['ethereum']['inr']
            }
        }
        return prices
    except Exception as e:
        print(f"Error fetching crypto prices: {e}")
        return None
