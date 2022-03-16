import spiders.spider
from utils.projectShow import start
from utils.projectShow import end
from spiders import spider
from spiders import spider2
from spiders import spider3


def start_spider():
    spider.crawl()
    spider2.crawl()
    spider3.crawl()


if __name__ == '__main__':
    start_spider()
