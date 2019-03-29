# -*- coding: utf-8 -*-
# encoding: utf-8

import scrapy
import re
import os
from scrapy import Spider, Request
from scrapy.utils.response import open_in_browser
from selenium import webdriver
from ScrapyDemo.items import ScrapyDemoItem
from datetime import datetime
import time

length=0

#print(help(webdriver.Chrome))
class demoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["xxx.com"]

    def __init__(self):
        print('-----spider initiated-----')
        self.browser = webdriver.Chrome(executable_path = '/usr/local/bin/chromedriver')
        self.browser.set_page_load_timeout(180)

    def closed(self, spider):
        print("-----spider closed666-----")
        self.browser.close()

    def start_requests(self):
        self.start_urls = ["http://www.xxx.com/"]
        for url in self.start_urls:
            url='http://www.xxx.com/'
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        #print(response.body)
        global i
        global length
        global lot_id_list, create_time_list, standard_product_id_list, title_list, main_image_list, seller_name_list, shipping_price_list, price_list, total_price_list, sold_count_list, ratings_count_string_list
        standard_product_id_list = []
        lot_id_list = []
        create_time_list = []
        title_list = []
        main_image_list = []
        seller_name_list = []
        shipping_price_list = []
        price_list = []
        total_price_list = []
        sold_count_list = []
        ratings_count_string_list = []
        i = 0
        item = ScrapyDemoItem()
        item['id'] =response.xpath('//div[@class="slot slot-auction placeholder"]/@id').extract() #提取id
        length = len(item['id'])

        print("-----show id number-----")
        print('total items: %s' % length)
        print("-----show id list-----")
        print(item['id'])
        #print(type(id_list))
        detail_url=[]

        #this link is parsed manually
        url_template = r'https://xxx.com/api/v1/lots/{}?source=%5Bobject+Object%5D&page=live_now&context=&module=&slot_template=&category_filters='
# -------------------------------------------------
        for i in range(int(length)):

        #for i in range(4):   #试

        #延时，price和total price在访问后需要大约3分钟才能从null变成具体数值
            if i==0:
                print('wait till price is loaded')
                time.sleep(180)
            #print(id_list[i])
            detail_url.append(url_template.format(item['id'][i]))
            yield Request(url=detail_url[i], meta={'item': item}, callback=self.detail_parse,encoding='utf-8')
            #print(detail_url)
        item['detail_link']=detail_url
#-------------------------------------------------

#还需要json提取出excel

    def detail_parse(self,response):

        item = response.meta['item']
        standard_product_id_list.append(response.xpath('//body/pre').re(r'"standard_product_id":\s*(\d{5,10}),"user_id":'))
        item['standard_product_id']=standard_product_id_list
        #item['standard_product_id']=response.xpath('//body/pre').re(r'"standard_product_id":\s*(\d{5,10}),"user_id":')

        lot_id_list.append(response.xpath('//body/pre').re('\d{9}')[0])
        item['lot_id'] = lot_id_list
        #item['lot_id']=response.xpath('//body/pre').re('\d{9}')[0]

        createtime=response.xpath('//body/pre').re('\d{4}-\d{2}-\d{2}T\d{2}.\d{2}.\d{2}')[1]
        create_time_list.append(str(datetime.strptime(createtime, "%Y-%m-%dT%H:%M:%S")))
        item['create_time'] = create_time_list
        #item['create_time']=str(datetime.strptime(createtime, "%Y-%m-%dT%H:%M:%S"))

        title_list.append(response.xpath('//body/pre').re(r'"title":"\s*(.*)","tax'))
        item['title']= title_list
        #item['title']=response.xpath('//body/pre').re(r'"title":"\s*(.*)","tax')

        main_image_list.append(response.xpath('//body/pre').re(r'"main_image":"\s*(.*.jpg)"'))
        item['main_image'] = main_image_list
        #item['main_image']=response.xpath('//body/pre').re(r'"main_image":"\s*(.*.jpg)"')

        seller_name_list.append(response.xpath('//body/pre').re(r'"seller_name":"\s*(.*)","seller'))
        item['seller_name']=seller_name_list
        #item['seller_name']=response.xpath('//body/pre').re(r'"seller_name":"\s*(.*)","seller')

        shipping_price_list.append(response.xpath('//body/pre').re(r'"shipping_price":"\s*(.*)","shipping'))
        item['shipping_price']=shipping_price_list
        #item['shipping_price']=response.xpath('//body/pre').re(r'"shipping_price":"\s*(.*)","shipping')

        sold_count_list.append(response.xpath('//body/pre').re(r'"starting_bid_amount":\s*(.*),"starting_bid_amount_local'))
        item['sold_count']=sold_count_list
        #item['sold_count']=response.xpath('//body/pre').re(r'"starting_bid_amount":\s*(.*),"starting_bid_amount_local')

        ratings_count_string_list.append(response.xpath('//body/pre').re(r'"ratings_count_string":"\s*(.*)","ratings_average'))
        item['ratings_count_string']=ratings_count_string_list
        #item['ratings_count_string']=response.xpath('//body/pre').re(r'"ratings_count_string":"\s*(.*)","ratings_average')

        price_list.append(response.xpath('//body/pre').re(r'"buy_now_price_with_symbol":"\s*(.*)","retail_price"'))
        item['price'] = price_list
        #item['price']=response.xpath('//body/pre').re(r'"buy_now_price_with_symbol":"\s*(.*)","retail_price"')

        total_price_list.append(response.xpath('//body/pre').re(r'"hammer_price":"\s*(.*)","hammer'))
        item['total_price'] = total_price_list
        #item['total_price']=response.xpath('//body/pre').re(r'"hammer_price":"\s*(.*)","hammer')

        #可以再这里加上：如果为null则重新访问 waiting to be implemented

#--------------------------------------------------------
        if len(ratings_count_string_list)==length:
        #if len(ratings_count_string_list) == 4:
            print("-----show item-----")
            print(item['id'])
            print(item['detail_link'])
            print(item['lot_id'])
            print(item['create_time'])
            print(item['title'])
            print(item['main_image'])
            print(item['seller_name'])
            print(item['shipping_price'])

            #空数据不能放入数据库
            for i in range(length):
            #for i in range(length):
                if item['standard_product_id'][i]==[]:
                    item['standard_product_id'][i]=['null']
                if item['price'][i]==[]:
                    item['price'][i]=['null']
                if item['ratings_count_string'][i]==[]:
                    item['ratings_count_string'][i]=['null']

            print(item['price'])
            print(item['ratings_count_string'])
            print(item['standard_product_id'])

            print(item['total_price'])
            print(item['sold_count'])
            #print('-------------end-------------')


        yield item
#把这个变成列表的形式 现在是item只有一个值