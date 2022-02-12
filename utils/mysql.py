from configparser import ConfigParser

import pymysql
from pymysql import MySQLError
from utils.convert import sql_str
from utils.convert import tuple_to_dataFrame
from pandas import DataFrame

class Mysql:
    def __init__(self):
        cfg = ConfigParser()
        cfg.read("../conf/config.cfg")
        host = cfg.get('Mysql', 'host')
        user = cfg.get('Mysql', "user")
        password = cfg.get('Mysql', "password")
        database = cfg.get('Mysql', "database")
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.flag = 0

    # 建立连接
    def connect(self):
        try:
            db = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.user,
                database=self.database
            )
        except MySQLError:
            print("数据库建立连接失败")
            self.flag = 1
            db = 0
        return db

    # 查询
    def query(self, tableName):
        db = self.connect()
        cursor = db.cursor()
        # tableName = "report"
        querySql = "select column_name from information_schema.columns where table_name = {0}".format(sql_str(tableName))
        querySql2 = "select * from {0}".format(tableName)
        res3 = DataFrame()

        try:
            # keyTuple
            cursor.execute(querySql)
            res = cursor.fetchall()
            # valueTuple
            res2 = cursor.execute(querySql2)
            res2 = cursor.fetchall()
            # dataFrame
            res3 = tuple_to_dataFrame(res,res2)
            # print()
            # for index1, row in enumerate(res):
            #     for index2, col in enumerate(row):
            #         print(str(index1 + 1) + "--" + str(index2 + 1) + "--" + str(col))
            db.close()
        except MySQLError:
            db.rollback()
            print("查询执行失败")
            self.flag = 1
        finally:
            return res3

    # 插入
    def insert(self, tableName, keyList, valueList):
        db = self.connect()
        if not db:
            self.flag = 1
            return 0
        cursor = db.cursor()
        # print("ok")
        strKeys = ",".join(keyList)
        # print(strKeys)
        strValues = ",".join(valueList)
        insertSql = "insert into {0}({1}) values({2})".format(tableName, strKeys, strValues)
        # print(insertSql)

        try:
            cursor.execute(insertSql)
            db.commit()
            db.close()

        except MySQLError:
            db.rollback()
            print("插入失败")
            self.flag = 1

    # 删除表
    def drop_table(self, tableName):
        db = self.connect()
        cursor = db.cursor()
        dropSql = "drop table if exists {0}".format(tableName)
        try:
            cursor.execute(dropSql)
            db.commit()
            db.close()
        except MySQLError:
            db.rollback()
            print("丢弃整张表失败")
            self.flag = 1

    # 创建表
    def create_table(self, tableName, keyList, typeList):
        db = self.connect()
        cursor = db.cursor()
        value = []
        for i in range(0, len(keyList)):
            item = [keyList[i], typeList[i]]
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

    # 状态
    def check_flag(self):
        return self.flag

    # 加载配置
    def load(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
