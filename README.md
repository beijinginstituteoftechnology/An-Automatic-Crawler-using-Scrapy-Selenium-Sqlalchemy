# An Automatic Crawler Scrapy Selenium Sqlalchemy



Crawler for JavaScript &amp; AJAX websites; Auto log in; Parse js; Save items into db; Auto load;  

可爬取两层需要登录的动态js渲染网站的爬虫，自动登录，解析js，自动存储数据库，自动循环加载爬虫。
  
# Note:  
Run perfectly.  
However, For privacy, the crawled website was changed to www.xxx.com, and the cookie used for login and the password for connecting to the database had been deleted.  
  
# How to run:  
Run main.py or open Scrapydemo.spiders.demo terminal and enter “scrapy crawl demo”.  
  
# Principles:  
1. Log in using selenium webdriver. add_cookie: In middleware: parse the JS login entry, use cookie, split the cookie and load, and then refresh.
2. Use Selenium and XPath to parse the primary page: after login, selenium can display the contents loaded by js. Use XPath to parse ID.
3. Use XPath to parse the second page and store the item. Since we already stores two items in first tier, in order to ensure the number of items entering pipeline is consistent, I use tables to append and then assign them to items.
4. Store into database: Use Sqlalchemy.ORM to connect to the database and put in the data.
5. Auto-loading crawler: This code is from online, no more explanation.
  
  
# 注：  
完美运行。  
然而为了隐私，爬取的网站改为了 www.xxx.com, 登录用的cookie和连接数据库的密码已被删掉。  
  
# 如何使用：  
运行main.py 或 打开Scrapydemo.spiders.demo terminal输入 “scrapy crawl demo”。  
  
# 原理：
1. 利用selenium webdriver driver.add_cookie登录：在middlewares中解析js登录入口，使用cookie，将cookie split后加载，并且refresh。
2. Selenium，xpath解析初级页面：登陆之后，selenium可显示出js加载的内容。利用xpath解析出id。
3. xpath解析第二层页面，存入item。由于第一层已经存储了两个item，为了保证每个item数目进入到pipeline数目保持一致，我利用表格append然后在赋值给item。
4. 存入数据库：数据进入pipeline，利用Sqlalchemy.orm连接数据库，放入数据。
5. 自动加载爬虫：此段代码来自于网络，不过多讲解。
