use weather;

# Deleting the transaction data from weather_trans type = hourly
delete from weather_trans where dt < CurDate() - 7 and type = "hourly" ;

# Deleting the transaction data from weather_trans type = daily
delete from weather_trans where dt < CurDate() - 31 and type = "daily" ;
