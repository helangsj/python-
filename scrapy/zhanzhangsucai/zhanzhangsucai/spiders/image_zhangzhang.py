import scrapy
from zhanzhangsucai.items import ZhanzhangsucaiItem

class ImageZhangzhangSpider(scrapy.Spider):
    name = 'image_zhangzhang'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        all_div = response.xpath('//*[@id="container"]/div')
        for div in all_div:
            item =  ZhanzhangsucaiItem()
            image_name = div.xpath('./p/a/text()').extract_first()
            #这里使用src2是因为图片懒加载，加载时图片和后面未加载图片名称不一样导致
            imgage_url = 'https:' + div.xpath('./div/a/img/@src2').extract_first()
            item['image_name'] = image_name
            item['imgage_url'] = imgage_url
            # print(imgage_url)
            #返回管道类
            yield item
