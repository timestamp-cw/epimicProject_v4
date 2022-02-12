from pyecharts.charts import Line

def line_chart(keyList:list,valueList:list):
    dataDict = {}
    line = Line()
    # print(type(valueList[:][1]))
    print(valueList)
    # for i in range(1,len(keyList)):
    #     dataDict[keyList[i]] = valueList[:][i]
    #     line.add_xaxis(keyList[i],valueList[i][])
