# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class ScrapydemoPipeline(object):
    Base = declarative_base()
    class User(Base):
        # 表的名字:
        __tablename__ = 'xxx'
        id = Column(String(10), primary_key=True)
        detail_link = Column(String(100))
        standard_product_id = Column(String(10))
        lot_id = Column(String(20))
        create_time = Column(String(20))
        title = Column(String(100))
        main_image = Column(String(100))
        seller_name = Column(String(20))
        shipping_price = Column(String(10))
        price = Column(String(10),nullable=True)
        total_price = Column(String(10))
        sold_count = Column(String(10))
        ratings_count_string = Column(String(10))

    def __init__(self):
        # 连接数据库 密码替换为你的password
        self.engine = create_engine('mysql://root:your password@localhost:3306/testtable')
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        print('-----pipeline is active-----')

    def process_item(self, item, spider):  # 爬取过程中执行的函数
        #print(spider.name)
        from ScrapyDemo.spiders.demo import length

        #判断item表是否满了
        if len(item['create_time'])==length:
        #if len(item['create_time']) == 3:
            #print('------------------now into database-------------------------')
            for i in range(length):
            #for i in range(3):
                new_user = self.User(

                    id=item['id'][i],
                    # id=item['id_new'][i],
                    detail_link=item['detail_link'][i],
                    standard_product_id=item['standard_product_id'][i],
                    lot_id=item['lot_id'][i],
                    create_time=item['create_time'][i],
                    title=item['title'][i],
                    main_image=item['main_image'][i],
                    seller_name=item['seller_name'][i],
                    shipping_price=item['shipping_price'][i],
                    price=item['price'][i],  ###不能是none：[[], [], [u'$14']] 否则会报错
                    total_price=item['total_price'][i],
                    sold_count=item['sold_count'][i],
                    ratings_count_string=item['ratings_count_string'][i]
                )
                self.session.add(new_user)
        try:
            self.session.commit()
            print('-----already into database-----')
        except:
            self.session.rollback()
            print('-----rollback-----')


    def close_spider(self, spider):  # 关闭爬虫时
        self.session.close()