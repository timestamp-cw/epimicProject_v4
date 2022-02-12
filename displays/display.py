import pandas
from pyecharts import options as opts
from pyecharts.charts import Line
from utils.convert import dataFrame_to_KVList

def show():
    # url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
    # data = pandas.read_json(url)
    data = pandas.read_json("../files/data.json")
    newIndex = pandas.to_datetime(data.index,)
    [keyList, valueList] = dataFrame_to_KVList(data, "date")
    print(keyList)
    print(valueList)

