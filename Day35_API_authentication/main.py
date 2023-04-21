import requests

# Add the API_KEY into the env variables
# export WEATHER_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# API_KEY = os.environ.get("WEATHER_API_KEY")
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 1.322762,
    "lon": 103.741124,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

print(data)
