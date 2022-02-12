import pandas
from utils.storeData import store_data
from utils.convert import dataFrame_to_KVList
from utils.mysql import Mysql
from utils.default import default_typelist
from urllib import request
import json

def crawl():
    # 处理disease.sh接口数据
    urlList = ["https://disease.sh/v3/covid-19/historical/all?lastdays=all",
               "https://disease.sh/v3/covid-19/all",
               "https://disease.sh/v3/covid-19/countries/usa",
               "https://disease.sh/v3/covid-19/vaccine/coverage/countries?lastdays=1"]

    resp = request.urlopen(urlList[1])
    data = json.loads(resp.read().decode("utf8"))

    # data = pandas.read_json("https://disease.sh/v3/covid-19/all")
    print(data)
    
    # data = pandas.read_json(urlList[0])
    # [keyList, valueList] = dataFrame_to_KVList(data, "date")
    # tableName = "historicalTable"
    # mysql = Mysql()
    # typeList = default_typelist(keyList)
    # mysql.create_table(tableName, keyList, typeList)
    # for value in valueList:
    #     mysql.insert(tableName, keyList, value)

crawl()