import scrapy
from qiushibaike.items import QiushibaikeItem

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # print(response)
        div_lists = response.xpath('//*[@id="content"]/div/div[2]/div')
        # print(div_lists)
        all_data = []
        for div in div_lists:
            #选取列表第一个元素转化为哦字符串
            # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            #直接选取第一个元素转换为字符串
            author = div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span/h2/text()').extract_first()
            #返回一个列表字符串
            page_text = div.xpath('./a[1]/div/span/text() ').extract()
            #使用join方法将列表转换为字符串
            page_text = ''.join(page_text)
            # print(author,page_text)
            #基于终端存储
        #     dic = {
        #         'author':author,
        #         'page_text':page_text
        #     }
        #     all_data.append(dic)
        # return all_data
            #基于管道
            item = QiushibaikeItem()
            item['author'] = author
            item['page_text'] = page_text
            #将item提交到管道
            yield item

