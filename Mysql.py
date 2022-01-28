import pymysql
from pymysql import MySQLError


class Mysql:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.flag = 0

    def Connect(self):
        try:
            db = pymysql.connect(
                host="localhost",
                user="wangchao",
                password="wangchao",
                database="test"
            )
        except MySQLError:
            print("数据库建立连接失败")
            self.flag = 1
            db = 0
        return db

    def Query(self, tableName):
        db = self.Connect()
        cursor = db.cursor()
        # tableName = "report"
        querySql = "select * from {0}".format(tableName)
        try:
            cursor.execute(querySql)
            res = cursor.fetchall()
            for index1, row in enumerate(res):
                for index2, col in enumerate(row):
                    print(str(index1 + 1) + "--" + str(index2 + 1) + "--" + str(col))
            db.close()
        except MySQLError:
            db.rollback()
            print("查询执行失败")
            self.flag = 1

    def Insert(self, tableName, keys,results):
        db = self.Connect()
        if not db:
            self.flag = 1
            # print("shibai ")
            return 0
        cursor = db.cursor()
        # 构造insertSql语句
        # tableName = "report"
        # keys = ["date", "content"]
        # results = ["'2021-01-01'", "'王超是个猪'"]
        strKeys = ",".join(keys)
        # print(results)
        strResults = ",".join(results)
        # print(strResults)
        insertSql = "insert into {0}({1}) values({2})".format(tableName, strKeys, strResults)

        # 插入
        try:
            cursor.execute(insertSql)
            db.commit()
            db.close()

        except MySQLError:
            db.rollback()
            print("插入失败")
            self.flag = 1

    def DropTable(self,tableName):
        db = self.Connect()
        cursor = db.cursor()
        # tableName = "report"
        dropSql = "drop table if exists {0}".format(tableName)
        try:
            cursor.execute(dropSql)
            db.commit()
            db.close()
        except MySQLError:
            db.rollback()
            print("丢弃整张表失败")
            self.flag = 1

    def CreateTable(self,tableName,keys,types,nulls):
        db = self.Connect()
        cursor = db.cursor()
        # tableName = "report"
        # keys = ["date", "content"]
        # types = ["varchar(255)", "text"]
        # nulls = ["not null", ""]
        value = []
        for i in range(0, len(keys)):
            item = [keys[i], types[i], nulls[i]]
            strItem = " ".join(item)
            value.append(strItem)
        strValue = ",".join(value)
        createSql = "create table {0}({1})".format(tableName, strValue)
        try:
            cursor.execute(createSql)
            db.commit()
            db.close()
        except MySQLError:
            db.rollback()
            print("创建数据表失败")
            self.flag = 1

    def check_flag(self):
        return self.flag
