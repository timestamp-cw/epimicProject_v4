import pandas
from pyecharts import options as opts
from pyecharts.charts import Line
from utils.mysql import Mysql

# 2020年到2022年全球疫情折线图
def show():
    # url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
    # data = pandas.read_json(url)
    # data = pandas.read_json("./data.json")
    mysql = Mysql()
    data = mysql.query("historicaltable")
    cases = data.get("cases").tolist()
    deaths = data.get("deaths").tolist()
    recovered = data.get("recovered").tolist()
    # timestampList = data.index.values.tolist()
    timestampList = data.get("date").tolist()
    dates = []
    for timestamp in timestampList:
        date = pandas.to_datetime(timestamp, format="%Y-%m-%d")
        strDate = str(date)[0:10]
        dates.append(strDate)

    line = (
        Line()
        .add_xaxis(dates)
        .add_yaxis("cases",cases)
        .add_yaxis("deaths",deaths)
        .add_yaxis("recovered",recovered)
        .set_global_opts(title_opts=opts.TitleOpts("2020年到2022年全球疫情折线图"))
    )
    line.render("../result/2020年到2022年全球疫情折线图.html")
    print("display successful")

show()