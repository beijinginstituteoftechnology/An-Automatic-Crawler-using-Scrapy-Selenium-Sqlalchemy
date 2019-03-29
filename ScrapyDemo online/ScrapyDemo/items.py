# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()  # id
    detail_link = scrapy.Field()  # detail链接
    standard_product_id=scrapy.Field()
    lot_id=scrapy.Field()
    create_time=scrapy.Field()
    title=scrapy.Field()
    main_image=scrapy.Field()
    seller_name=scrapy.Field()
    shipping_price=scrapy.Field()
    price=scrapy.Field()
    total_price=scrapy.Field()
    sold_count=scrapy.Field()
    ratings_count_string=scrapy.Field()
    pass
