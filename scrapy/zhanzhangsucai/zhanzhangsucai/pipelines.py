# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class ZhanzhangsucaiPipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.images import ImagesPipeline
import scrapy
class imagesPiplines(ImagesPipeline):
    #方法重写.根据图片地址进行数据的请求
    def get_media_requests(self,item,info):
        #使用meta来进行传参
        yield scrapy.Request(item['imgage_url'], meta={'item':item})
    #指定图片存储路径
    def file_path(self, request, response=None, info=None,item=None):
        item = request.meta['item']
        imaName = item['image_name'] + '.jpg'
        # imaName = request.url.split('/')[-1]
        print(imaName)
        return imaName

    def item_completed(self, results, item, info):
        return item