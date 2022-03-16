from pyhive import hive

PORT = 10000
name = "root"
password = "123456"
host = "192.168.17.111"
database = "pro"
auth = "LDAP"
conn = hive.Connection(host=host, port=PORT, username=name, database=database, auth=auth, password=password)

cursor = conn.cursor()
cursor.execute("show tables")
# for result in cursor.fetchall():
#     print(result)