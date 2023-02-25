import requests
import time
from datetime import datetime

def get_weather(city):

    #import data from openweather
    
    ## input your API_KEY FROM https://openweathermap.org/ to appid
    appid = ""
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=metric'

    r = requests.get(URL)
    rjson = r.json()
    # save weather data
    condition = rjson['weather'][0]['main']
    description = rjson['weather'][0]['description']

    # temp info
    temp = rjson['main']['temp']
    temp_min = rjson['main']['temp_min']
    temp_max = rjson['main']['temp_max']

    # wind info
    wind_speed = rjson['wind']['speed']

    # sunrise and sunset
    sunrise = rjson['sys']['sunrise']
    sunset = rjson['sys']['sunset']
    # to int for datetime
    sun_rise = int(sunrise)
    sun_set = int(sunset)

    #humidity and preassure
    humidity = rjson['main']['humidity']
    preassure = rjson['main']['pressure']

    # print weather
    print("Weather today: {}\n".format(description))
    print("The temperature should be around: {}°C\nmax.temp: {}°C and min_temp: {}°C ".format(temp, temp_max, temp_min))
    print(" ")
    print("Wind speed: {} m/s".format(wind_speed))
    print(" ")
    print("Sunrise will be at: " + datetime.utcfromtimestamp(sun_rise).strftime('%H:%M:%S') + " UTC time")
    print("Sunset will be at: " + datetime.utcfromtimestamp(sun_set).strftime('%H:%M:%S') + " UTC time")
    print(" ")
    print("Humidity {}%, Preassure: {} hPa".format(humidity, preassure))
while True:
    get_weather(input("city: "))
    time.sleep(60)

