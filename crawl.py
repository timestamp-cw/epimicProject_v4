from lxml import html
from queue import Queue
from time import sleep
import re
from Mysql import Mysql
from configparser import ConfigParser
import shutil
import os
from pymysql import MySQLError


def spider():
    start_url = "http://www.gov.cn/xinwen/2022-01/05/content_5666479.htm"
    base_url = "http://www.gov.cn"
    queue1 = Queue(10)
    queue1.put(start_url)
    pattern1 = re.compile(r"\d+")
    count = 0
    while not queue1.empty():
        url = queue1.get()
        print(url)
        sleep(1)
        title_list = pattern1.findall(url)
        filename = "-".join(title_list)
        htmlElem = html.parse(url, parser=html.HTMLParser())
        text = htmlElem.xpath("//div[@id='UCAP-CONTENT']//text()")
        result = "".join(text).strip()
        # 存储数据
        store_data(filename, result)
        #
        link = htmlElem.xpath("//ul[@class='list01']//a/@href")[0]
        new_url = base_url + link
        queue1.put(new_url)
        count += 1
        if count == 3:
            break


def store_data(title, text):
    # 存储到数据库 report表
    cfg = ConfigParser()
    cfg.read("./config.cfg")
    host = cfg.get('Mysql', 'host')
    user = cfg.get('Mysql', "user")
    password = cfg.get('Mysql', "password")
    database = cfg.get('Mysql', "database")
    mysql = Mysql(
        host=host,
        user=user,
        password=password,
        database=database
    )
    strTitle = "'" + title + "'"
    strText = "'" + text + "'"
    result = [strTitle, strText]
    tableName = "report"
    keys = ["date", "content"]
    mysql.Insert(tableName, keys,result)
    # mysql.Query(tableName)
    exitflag = mysql.check_flag()

    if exitflag:
        # 存储为TXT文本
        if not os.path.exists("./store"):
            os.mkdir("./store")
        else:
            print("os 文件夹存在")
        with open("./store/" + title + ".txt", "w",encoding="utf8") as fp:
            fp.write(text)
        # if os.path.exists("./store"):
        #     shutil.rmtree("./store")
        # else:
        #     print("shutil 文件夹不存在")
