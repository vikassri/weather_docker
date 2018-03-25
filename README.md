# weather_docker

This project is for downloading the creating the data pipeline of weather data to mysql.

Historical - https://data.gov.uk/dataset/

Daily/forecast - https://openweathermap.org/

# Dataset

Historical - Downloading the data historical data of 5 cities of UK
Daily - Downloading the daily dataset of those 5 cities
Hourly/Forecast - Download the forecast data of 5 cities of 5 days as forecast of every 3 hour.

# fields:

date - date of the records
tmax - maximum temperature of the day / 3 hour in Degree Celsius
tmin - mimimum temperature of the day / 3 hour in Degree Celsius
rain - rain in mm
hour - hour of the date
city - selfexplainatory
type - hourly/daily

# Data Cleansing

Delete the row of more than 3 blank value
changing the some NA values with the mean of the column
remove the unwanted values from the data
converting them into utf-8
Dropping the unwanted column from the dataset like af/sun
Description

Used python api of the weather to download the dataset and stored into relational database like mysql, As the dataset is small RDBMS is very good for it, Once the size started growing we can switch to any other database like hive/hbase.

# Retention

Hourls - last 5 days should be available
Daily - last 30 days should be available

######    Docker Commands  ######
# Run Weather.sh  (this will create the docker and login for you) 
  sh weather.sh 
  
#  docker created run the below script
1. cd /home/scripts
2. sh run.sh


