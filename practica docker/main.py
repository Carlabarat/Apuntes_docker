import requests

response = requests.get("https://catfact.ninja/fact")
print(response)
data=response.json()
print(data)
