import json
import pandas
from pyecharts.charts import Map
from pyecharts import options as opts
from urllib import request
from utils.convert import dataFrame_to_KVList
from utils.mysql import Mysql
from utils.default import default_typelist

url ="https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"
resp = request.urlopen(url)
data = json.loads(resp.read().decode("utf8"))
provinceCompare = data['data']['provinceCompare']
# print(provinceCompare)
uu = pandas.DataFrame(provinceCompare)
frameTable = uu.transpose()
# print(uu.transpose())
item = dataFrame_to_KVList(frameTable, "province")
print(item)
mysql = Mysql()
tableName = "province"
typeList = default_typelist(item[0])
mysql.create_table(tableName, item[0], typeList)
keyList = item[0]
for value in item[1]:
    mysql.insert(tableName, keyList, value)