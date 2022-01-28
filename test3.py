from Mysql import Mysql
mysql = Mysql(
    host="localhost",
    user="wangchao",
    password="wangchao",
    database="test"
)
mysql.Insert()
mysql.Query()