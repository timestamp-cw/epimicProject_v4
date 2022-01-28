from Mysql import Mysql
mysql = Mysql(
    host="localhost",
    user="wangchao",
    password="wangchao",
    database="test"
)
tableName = "testTable1"
# tableName = "report"
keys = ["date", "content"]
types = ["varchar(255)", "text"]
nulls = ["not null", ""]
mysql.CreateTable(tableName,keys,types,nulls)
mysql.DropTable(tableName)