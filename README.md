# weather_docker

This project is for downloading the creating the data pipeline of weather data to mysql.

1. Historical - https://data.gov.uk/dataset/

2. Daily/forecast - https://openweathermap.org/

# Dataset

1. Historical - Downloading the data historical data of 5 cities of UK
2. Daily - Downloading the daily dataset of those 5 cities
3. Hourly/Forecast - Download the forecast data of 5 cities of 5 days as forecast of every 3 hour.

# fields:

1. date - date of the records
2. tmax - maximum temperature of the day / 3 hour in Degree Celsius
3. tmin - mimimum temperature of the day / 3 hour in Degree Celsius
4. rain - rain in mm
5. hour - hour of the date
6. city - selfexplainatory
7. type - hourly/daily

# Data Cleansing

1. Delete the row of more than 3 blank value
2. changing the some NA values with the mean of the column
3. remove the unwanted values from the data
4. converting them into utf-8
5. Dropping the unwanted column from the dataset like af/sun

# Description

Used python api of the weather to download the dataset and stored into relational database like mysql, As the dataset is small RDBMS is very good for it, Once the size started growing we can switch to any other database like hive/hbase.

# Retention

1. Hourls - last 5 days should be available
2. Daily - last 30 days should be available

######    Docker Commands  ######
# Run Weather.sh  (this will create the docker and login for you) 
  sh weather.sh 
  
#  docker created run the below script
1. cd /home/scripts
2. sh run.sh


