import requests

API_KEY = "ed4e5a3d8c0fc880d86006d7b66d5ce6"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200: #200 means sucessful
    data = response.json() #gives json data as python dictionary bc data is returned as json
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
else:
    print("An error occurred.")