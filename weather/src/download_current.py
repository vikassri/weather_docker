import requests
import json
import urllib.request
import datetime
from mysql_connection import *


def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I')
    return converted_time


def url_builder(city_id, user_api):
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.

    current_api = "http://api.openweathermap.org/data/2.5/weather?id="

    full_api_url = current_api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def parse_json(data):
    city_name = data['name']
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    hour = time_converter(data["dt"])
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_max"]
    if data["weather"][0]["icon"] in ['10d', '09d']:
        rain_mm = data["rain"]["3h"]
    else:
        rain_mm = 0
    columns = ("{},{},{},{},{},{},{}").format(dt, hour, temp_min, temp_max, rain_mm, "daily", city_name)
    conn = mysql_connection().connect()
    mysql_connection().insert_trans(tuple(columns.split(',')), conn)

if __name__ == '__main__':
    user_api = "52e1ab7d5d5d12a31d64d3e382eead66"
    city_list = {"bradford": 5907166, "eastbourne": 7290686, "heathrow:": 7284876, "oxford": 5956895,
                 "Southampton": 4951582}
    for city_name, city_id in city_list.items():
        parse_json(data_fetch(url_builder(city_id, user_api)))
        print("Count inserted for " + city_name )
