import pandas
from pyecharts import options as opts
from pyecharts.charts import Line
from utils.convert import dataFrame_to_KVList
from charts.line import line_chart

def show():
    # url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
    # data = pandas.read_json(url)
    data = pandas.read_json("../files/data.json")
    index = data.index.tolist()
    newIndex = [str(z)[0:10] for z in index]
    newSeries = pandas.Series(newIndex,index=index)
    data.insert(0,"date",newSeries)
    [keyList,valueList] = dataFrame_to_KVList(data,"index")
    line_chart(keyList,valueList)

    # print(keyList)
    # print(valueList)


show()
