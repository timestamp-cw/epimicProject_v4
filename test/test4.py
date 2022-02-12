import pandas
from utils.mysql import Mysql
from configparser import ConfigParser

# url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
# data = pandas.read_json(url)
data = pandas.read_json("../files/data.json")
cases = data.get("cases").tolist()
deaths = data.get("deaths").tolist()
recovered = data.get("recovered").tolist()
timestampList = data.index.values.tolist()
dates = []
for timestamp in timestampList:
    date = pandas.to_datetime(timestamp, format="%Y-%m-%d")
    strDate = str(date)[0:10]
    dates.append(strDate)

strCases = [str(cc) for cc in cases]
strDeaths = [str(dd) for dd in cases]
strRecovered = [str(rr) for rr in recovered]
strDates = ["'"+zz+"'" for zz in dates]
# print(strDates)

result = [list(z) for z in zip(strDates,strCases,strDeaths,strRecovered)]

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
tableName = "earthEpidmicTable"
keys = ["date","cases","deaths","recovered"]
for i in result:
    mysql.Insert(tableName,keys,i)

mysql.Query(tableName)



# line = (
#     Line()
#         .add_xaxis(dates)
#         .add_yaxis("cases", cases)
#         .add_yaxis("deaths", deaths)
#         .add_yaxis("recovered", recovered)
#         .set_global_opts(title_opts=opts.TitleOpts("2020年到2022年全球疫情折线图"))
# )
# line.render("2020年到2022年全球疫情折线图2.html")
# print("display successful")