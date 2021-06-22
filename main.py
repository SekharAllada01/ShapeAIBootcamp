import requests

from datetime import datetime

api_key = 'd71369a4b2b6127a8db78a54f7112c5e'

location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

with open('Weatherinfo.txt', 'w') as f:
    f.write("--------------------------------------------------------------------------------")
    f.write("\nWeather Stats for - {}||{}".format(location.upper(), date_time))
    f.write("\n-------------------------------------------------------------------------------")
    f.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
    f.write("\nCurrent weather desc  :{}".format(weather_desc))
    f.write("\nCurrent Humidity      :{}".format(hmdt)+"%")
    f.write("\nCurrent wind speed    :{}".format(wind_spd)+"kmph")
