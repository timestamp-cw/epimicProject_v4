import json
import pandas
from pyecharts.charts import Map
from pyecharts import options as opts
from urllib import request

url ="https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"
# with open("list.json", "r", encoding="utf8") as fp:
#     data = json.loads(fp.read())
resp = request.urlopen(url)
data = json.loads(resp.read().decode("utf8"))
chinaDayAddList = data['data']['chinaDayAddList']
chinaDayList = data['data']['chinaDayList']
nowConfirmStatis = data['data']['nowConfirmStatis']
provinceCompare = data['data']['provinceCompare']
xx = pandas.DataFrame(chinaDayAddList)
yy = pandas.DataFrame(chinaDayList)
# zz = pandas.DataFrame(nowConfirmStatis)
uu = pandas.DataFrame(provinceCompare)
keysList = uu.keys().tolist()
nowConfirm = uu.loc["nowConfirm"]
confirmAdd = uu.loc["confirmAdd"]
dead = uu.loc["dead"]
heal = uu.loc["heal"]
zero = uu.loc["zero"]
print(xx)
valueList = nowConfirm.values.tolist()
valueList2 = confirmAdd.values.tolist()
valueList3 = dead.values.tolist()
valueList4 = heal.values.tolist()
valueList5 = zero.values.tolist()
print(keysList)
print(valueList)

map = (
    Map()
    .add("nowConfirm", [list(z) for z in zip(keysList, valueList)], "china")
    .add("confirmAdd", [list(z) for z in zip(keysList, valueList)], "china")
    .add("head", [list(z) for z in zip(keysList, valueList)], "china")
    .add("heal", [list(z) for z in zip(keysList, valueList)], "china")
    .add("zero", [list(z) for z in zip(keysList, valueList)], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国疫情地图"),
        visualmap_opts=opts.VisualMapOpts(max_=550, split_number=10, is_piecewise=False))
)
map.render("中国疫情地图")