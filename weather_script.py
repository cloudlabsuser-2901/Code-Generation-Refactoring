import requests

def get_weather(city):
  API_KEY = '6c85e936d1a41164f6042359a544f970'
  BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
  response = requests.get(BASE_URL)
  data = response.json()
  main = data['main']
  print(f"Temperature: {main['temp']}")
  print(f"Humidity: {main['humidity']}")
  print(f"Weather: {data['weather'][0]['description']}")

city = input("Enter the city: ")
get_weather(city)