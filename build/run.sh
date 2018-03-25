#bin/bash

echo "restarting mysql-server"
/etc/init.d/mysql restart

echo "\n*********** creating mysql database and tables **********\n"
mysql -uroot -proot < /home/scripts/sql/create_table.sql
echo "Table created successfully : weather_trans "
echo "Table created successfully : weather_history"

cd src

echo "\n********** download the historical datase for 5 cities and loading into mysql ************\n"
python history_data_download.py

echo "\n********** downloading forecast data for next five days and loading into mysql transaction table *********\n"
python download_forecast.py

echo "\n*********** downloading the currect date data and load into mysql trans table ***********\n"
python download_current.py


echo """\n\nplease check the data in mysql
	mysql -uroot -proot

	use weather;
	select count(*),city_name from weather_history group by city_name ;
	select * from weather_history limit 10;
	select count(*),city_name from weather_trans group by city_name ;
	select * from weather_trans limit 10;

	For retention
	mysql -uroot -proot < /home/scripts/sql/retention.sql


"""


