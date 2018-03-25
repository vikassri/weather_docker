import pymysql.cursors


class mysql_connection:
    def __init__(self, host="localhost", user="root", passwd="root", db="weather", charset="utf8mb4"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    def connect(self):
        return pymysql.connect(host=self.host,
                               user=self.user,
                               password=self.passwd,
                               db=self.db,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

    def insert_trans(self, columns, connection):
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `weather_trans` (`dt`, `hour`, `tmax`, `tmin`, `rain`, `type`, `city_name`) VALUES (%s, %s, %s ,%s, %s, %s, %s)"
                cursor.execute(sql, columns)
            connection.commit()
        except IOError:
            print("Not able to insert the data")

    def insert_history(self, file, connection):
        try:
            count = 0
            with connection.cursor() as cursor:
                # Create a new record
                for line in open(file, "r").readlines():
                    columns = tuple(line.split(','))
                    sql = "INSERT INTO `weather_history` (`dt`, `tmax`, `tmin`, `rain`, `city_name`) VALUES (%s, %s, %s ,%s, %s)"
                    cursor.execute(sql, columns)
                    count += 1
                connection.commit()
            return count
        except IOError:
            print("Not able to insert the data")

    def query(self, connection):
        try:
            with connection.cursor() as cursor:
                sql = "show tables"
                cursor.execute(sql)
                return cursor.fetchall()
        except IOError:
            print("Not able to insert the data")
