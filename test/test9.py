from utils.mysql import Mysql
mysql = Mysql()
xx = mysql.query("report")
# from utils.convert import tuple_to_dataFrame
# a = ((1,2),("q","w"))
# b = (("qq","ww"))
# c = tuple_to_dataFrame(b,a)
# print(c)
# import pandas as pd
# res = pd.DataFrame(a,b)
# print(res.transpose())