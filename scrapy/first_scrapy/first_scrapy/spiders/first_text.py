import scrapy


class FirstTextSpider(scrapy.Spider):
    #代码唯一标识，爬虫文件名称
    name = 'first_text'
    #允许的域名，用来限定start_urls中访问的域名
    #allowed_domains = ['www.baidu.com']
    #访问地址列表
    start_urls = ['https://www.baidu.com/','http://www.sogou.com/']
    #用作于数据解析：response表示响应对象
    def parse(self, response):
        print(response)
