create database IF NOT EXISTS `weather`;

use weather;
CREATE TABLE IF NOT EXISTS `weather_history` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    dt date,
    tmax float,
    tmin float,
    rain float,
    city_name varchar(20),
    PRIMARY KEY (`id`)
);

CREATE TABLE `weather_trans` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
 	dt Date,
 	hour int(2),
    tmax float,
    tmin float,
    rain float,
    type varchar(10),
    city_name varchar(20),
    PRIMARY KEY (`id`)
);



