# -*- coding: utf-8 -*-
# encoding: utf-8

#可执行爬虫
#如果出现不存在MySQLdb 则在mysqldb.py改变return __import__("MySQLdb") 为 return __import__("pymysql")
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "demo"])

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import time
import logging
from scrapy.utils.project import get_project_settings

configure_logging()
runner = CrawlerRunner(get_project_settings())
j=0
@defer.inlineCallbacks
def crawl():
    global j
    while True:
        time_stamp=int(time.time())
        open_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time_stamp))
        print('-----round %s starts at %s-----' % (j,open_time))
        logging.info("new cycle starting")
        yield runner.crawl('demo')  #爬虫的名字
        from ScrapyDemo.spiders.demo import length
        print('-\n''--\n''---\n''----\n''-----total %s items are crawled in the round-----\n''----\n''---\n''--\n''-\n'
              % length)

        time_stamp = int(time.time())
        stop_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
        print('-----round %s ends at %s-----' % (j,stop_time))
        # 一分钟跑一次
        time.sleep(10)
        j+=1

    reactor.stop()


crawl()
reactor.run()