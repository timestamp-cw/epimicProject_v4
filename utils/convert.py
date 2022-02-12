from pandas import DataFrame
from pandas import Series

def dataFrame_to_KVList(dataframe: DataFrame, indexName) -> list:
    keyList = [indexName] + dataframe.keys().tolist()
    valueList = []
    for index in dataframe.index.tolist():
        value = [sql_str(str(index))] + [sql_str(str(z)) for z in dataframe.loc[index].tolist()]
        valueList.append(value)
    return [keyList, valueList]


def sql_str(text: str) -> str:
    return "'" + text + "'"

def tuple_to_dataFrame(res:tuple,res2:tuple) -> DataFrame:
    keyTuple = list(zip(*res))[0]
    dataFrame = DataFrame(res2,columns=keyTuple)
    return dataFrame
