import json
from urllib import request
import pandas

from utils.mysql import Mysql
from utils.convert import dataFrame_to_KVList
from utils.default import default_typelist


def crawl():
    # 处理腾讯疫情数据接口数据
    url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"
    resp = request.urlopen(url)
    data = json.loads(resp.read().decode("utf8"))
    # with open("../files/list.json","r",encoding="utf8") as fp:
    #     data = json.loads(fp.read())
    tableNameList = list(data['data'].keys())
    tableNameList.remove("nowConfirmStatis")
    itemList = []
    # print(tableNameList)
    for key in tableNameList:
        dictTable = data['data'][key]
        frameTable = pandas.DataFrame(dictTable)
        item = dataFrame_to_KVList(frameTable, "id")
        itemList.append(item)

    mysql = Mysql()

    for index, tableName in enumerate(tableNameList):
        typeList = default_typelist(itemList[index][0])
        mysql.create_table(tableName, itemList[index][0], typeList)
        keyList = itemList[index][0]
        for value in itemList[index][1]:
            mysql.insert(tableName, keyList, value)
