from urllib import response
import json
import requests
import os

def meteo(lat,lon,api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?"
    url = url + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key
    response = requests.get(url)
    data = json.loads(response.text)

    return data

def get_env():
    env= os.environ
    lattitude= env['LAT']
    longitude=env['LONG']
    api_key=env['API_KEY']

    return lattitude,longitude,api_key

if __name__=="__main__":
    lat,lon,api_key= get_env()
    Meteo=meteo(lat,lon,api_key)
    print(Meteo)

