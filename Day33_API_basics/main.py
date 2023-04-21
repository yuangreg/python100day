import requests

API_LINK = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat": 1.290270,
    "lng": 103.851959,
}
response = requests.get(url=API_LINK, params=parameters)
response.raise_for_status()
data = response.json()

print(data)
