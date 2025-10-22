
import requests
url ="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=USD"
response = requests.get(url)
data = response.json()
print(f"Bitcoin Price: ${data['bitcoin']['usd']}")
