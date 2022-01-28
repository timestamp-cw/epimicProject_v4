# from queue import Queue
# queue1 = Queue(10)
# for i in range(1,10):
#     queue1.put(i)
#
# while not queue1.empty():
#     print(queue1.get())
#
# import re
# url = "http://www.gov.cn/xinwen/2022-01/05/content_5666479.htm"
# pattern1 = re.compile(r"\d+")
# res = pattern1.findall(url)
# result = "-".join(res)
# print(result)
import pymysql
from pymysql import MySQLError



cursor = db.cursor()

querySql = "select version()"


tableName = "report"
keys = ["date", "content"]
results = ["'2021-01-01'", "'王超是个猪'"]
strKeys = ",".join(keys)
strResults = ",".join(results)
insertSql = "insert into {0}({1}) values({2})".format(tableName, strKeys, strResults)

# 插入
try:
    cursor.execute(insertSql)
    db.commit()
    db.close()

except MySQLError:
    db.rollback()
    print("插入失败")

# 查询
querySql = "select * from report"
try:
    cursor.execute(querySql)
    res = cursor.fetchall()
    for index1, row in enumerate(res):
        for index2, col in enumerate(row):
            print(str(index1 + 1) + "--" + str(index2 + 1) + "--" + col)

    db.close()
except MySQLError:
    print("语句执行失败")
