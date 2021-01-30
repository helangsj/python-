import scrapy


class XiaohuaproSpider(scrapy.Spider):
    name = 'xiaohuaPro'
    start_urls = ['http://www.521609.com/meinvxiaohua/']

    #创建新的地址
    url ='http://www.521609.com/meinvxiaohua/list12%d.html'
    pageNum = 2

    def parse(self, response):
        all_lis = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        for li in all_lis:
            ima_name = li.xpath('./a[2]/text()| ./a[2]/b/text()').extract_first()
            print(ima_name)
            #后面网页的url
        if self.pageNum <=3:
            new_url = format(self.url%self.pageNum)
            self.pageNum += 1
            #手动请求发送：callback回调函数是专门用作数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)
