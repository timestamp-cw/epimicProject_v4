# from lxml import html
# from lxml.html import etree
# import re
# htmlElem = html.parse("start.html",parser=html.HTMLParser())
# text = htmlElem.xpath("//div[@id='UCAP-CONTENT']//text()")
# result = "".join(text).strip()
# link = htmlElem.xpath("//ul[@class='list01']//a/@href")[0]
#
# print(link)
# print(result)

# content = etree.tostring(htmlElem,encoding="utf8")
# result = content.decode("utf8")
# pattern1 = re.compile(r"")
# print(result)


list1 = ["1","2","3"]
for index , i in enumerate(list1):
    print(str(index)+"---"+i)