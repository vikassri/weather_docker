import io

import numpy as np
import pandas as pd
import requests

from mysql_connection import *


def get_city_df(city_name):
    url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/" + city_name + "data.txt"
    try:
        s = requests.get(url).content
    except IOError:
        print("City Name is not correct")

    header = ["year", "month", "tmax", "tmin", "air_frost", "rain", "sun"]
    city_df = pd.read_fwf(io.StringIO(s.decode('utf-8')), skiprows=6, sep='\s+', header=0, keep_default_na=False,
                          na_values=[])
    city_df.columns = header
    city_df.replace("---", np.nan, inplace=True)
    city_df["city_name"] = city_name
    city_df['dt'] = city_df['year'].map(str) + "-" + city_df["month"].map(str) + "-01"
    city_df.drop(['year', 'month'], axis=1, inplace=True)
    # to fill the values with mean value of columns
    city_df = city_df[["dt","tmax","tmin","rain","city_name"]]
    return city_df.dropna()


if __name__ == '__main__':
    cities = ["Aberporth", "Armagh", "Bradford", "Camborne", "Heathrow"]
    conn = mysql_connection().connect()
    for city_name in cities:
        try:
            value = get_city_df(city_name.lower())
            value.to_csv("/home/data/" + city_name + ".csv", index=False, encoding='utf-8',header=False)
            print("Count for " + city_name + " : " , mysql_connection().insert_history("/home/data/" + city_name + ".csv", conn))
        except IOError:
            print("Not able to Download")
