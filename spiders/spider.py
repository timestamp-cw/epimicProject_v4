from lxml import html
from queue import Queue
from time import sleep
import re
from utils.mysql import Mysql
from utils.default import default_typelist


def crawl():
    # 抓取页面
    # 新型冠状病毒肺炎疫情最新情况  卫生健康委网站
    start_url = "http://www.gov.cn/xinwen/2022-01/05/content_5666479.htm"
    base_url = "http://www.gov.cn"
    queue1 = Queue(10)
    queue1.put(start_url)
    pattern1 = re.compile(r"\d+")
    count = 0
    filenameList = []
    resultList = []
    while not queue1.empty():
        url = queue1.get()
        print(url)
        sleep(1)
        title_list = pattern1.findall(url)
        filename = "-".join(title_list)
        htmlElem = html.parse(url, parser=html.HTMLParser())
        text = htmlElem.xpath("//div[@id='UCAP-CONTENT']//text()")
        result = "".join(text).strip()
        strFilename = "'" + filename + "'"
        strResult = "'" + result + "'"
        filenameList.append(strFilename)
        resultList.append(strResult)
        link = htmlElem.xpath("//ul[@class='list01']//a/@href")[0]
        new_url = base_url + link
        queue1.put(new_url)
        count += 1
        if count == 3:
            break

    keyList = ["date", "content"]
    valueList = [list(z) for z in zip(filenameList, resultList)]
    tableName = "report"
    mysql = Mysql()
    typeList = default_typelist(keyList)
    mysql.create_table(tableName, keyList, typeList)
    for value in valueList:
        mysql.insert(tableName, keyList, value)
