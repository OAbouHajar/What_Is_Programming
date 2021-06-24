import requests
import json

city = input('please enter the city you want: ')

url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city+ '&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'

data = requests.get(url)
data_json = data.json()

print(data_json['name'])
print(data_json['weather'][0]['description'])
print('Temp: ',data_json['main']['temp'])
print('Feels Like: ',data_json['main']['feels_like'])
print('Humidity: ',data_json['main']['humidity'])