# we import requests library (someone's work)
import requests

# we take the city as a user input 
city = input('please enter the city you want to check the weather for: ')

# we save the respond from get into r
r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1')

# we convert r into jason and save it inside weather_data
wather_data = r.json()
# row data coming from the link
print(wather_data)
# here we print to the user nicely
print('*********** DATA TO USER *************')
print('Country: ', wather_data['sys']['country'])
print('City: ', wather_data['name'])
print('Temp: ',wather_data['main']['temp'])
if int(wather_data['main']['temp']) > 15:
    print('Summer is Here - SUN')
print('Humidity: ', wather_data['main']['humidity'])
print('Weather Description:  ', wather_data['weather'][0]['description'])