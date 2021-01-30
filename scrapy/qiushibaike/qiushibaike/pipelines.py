# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiushibaikePipeline (object):
    fp = None
    def open_spider(self,  spider):
        print('开始爬虫……')
        self.fp = open('./qiushi.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        author = item['author']
        page_text = item['page_text']
        # if type(author)=='NoneType' or type(page_text) == 'NoneType':
        #     author = '匿名用户'
        #     page_text = ''
        print(author,page_text)
        self.fp.write(author + ':' + page_text)
        return item #这个item回传给下一个管道类
    def close_spider(self,spider):
        print('结束爬虫.')
        self.fp.close()
import pymysql
#管道文件中一个管道类将一组数据存储到一个平台或载体中
class mysqlQiushibaikePipeline (object):
    conn = None
    cur = None
    def open_spider(self, spider):
        print('开始存入数据库……')
        self.conn = pymysql.connect(host = '127.0.0.1',port=3306,user='root',password='root',db='python',charset='utf8')

    def process_item(self, item, spider):
        #打开游标
        self.cur = self.conn.cursor()
        #插入值
        try:
         self.cur.execute('insert into qiushi VALUES ("%s","%s")'%(item['author'],item['page_text']))
         self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        # author = item['author']
        # page_text = item['page_text']

        return item  # 这个item回传给下一个管道类

    def close_spider(self, spider):
        print('存入数据库完成.')
        self.cur.close()
        self.conn.close()