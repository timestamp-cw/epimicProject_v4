from configparser import ConfigParser
from utils.mysql import Mysql


def store_data(keyList,valueList,tableName):
    # 加载数据库配置
    mysql = Mysql()
    mysql.insert(tableName, keyList,valueList)
    # mysql.Query(tableName)
    # exitFlag = mysql.check_flag()
    #
    # if exitFlag:
    #     # 存储为TXT文本
    #     if not os.path.exists("../store"):
    #         os.mkdir("../store")
    #     else:
    #         print("os 文件夹存在")
    #     with open("./store/" + valueList[0] + ".txt", "w",encoding="utf8") as fp:
    #         fp.write(valueList[1])
    #     if os.path.exists("./store"):
    #         shutil.rmtree("./store")
    #     else:
    #         print("shutil 文件夹不存在")
