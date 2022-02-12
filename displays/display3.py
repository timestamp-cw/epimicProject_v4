from utils.mysql import Mysql
from pyecharts.charts import Map
from pyecharts import options as opts

def show():

    mysql = Mysql()
    data = mysql.query("provincecompare")
    data = data.drop(columns="id")
    print(data)
    keysList = data.keys().tolist()
    valueList = data.loc[0].tolist()
    valueList2 = data.loc[1].tolist()
    valueList3 = data.loc[2].tolist()
    valueList4 = data.loc[3].tolist()
    valueList5 = data.loc[4].tolist()
    print(valueList)


    map = (
        Map()
        .add("nowConfirm", [list(z) for z in zip(keysList, valueList)], "china")
        # .add("confirmAdd", [list(z) for z in zip(keysList, valueList2)], "china")
        # .add("head", [list(z) for z in zip(keysList, valueList3)], "china")
        # .add("heal", [list(z) for z in zip(keysList, valueList4)], "china")
        # .add("zero", [list(z) for z in zip(keysList, valueList5)], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国疫情地图"),
            visualmap_opts=opts.VisualMapOpts(max_=550, split_number=10, is_piecewise=False))
    )
    map.render("../result/中国疫情地图.html")


show()