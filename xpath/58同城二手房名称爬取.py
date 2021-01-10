import requests
from lxml import etree

if __name__ == "__main__":
    url = 'https://bj.58.com/ershoufang/'
    headers = {'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.88Safari / 537.36'
    }
    response = requests.get(url=url,headers=headers).text
    #将数据放入etree中
    response_etree = etree.HTML(response)
    #获取所有的列表
    all_house_name = response_etree.xpath('//ul[@class="house-list-wrap"]/li')
    #数据存储
    fp = open('58同城名字.text','w',encoding='utf-8')
    for house_name in all_house_name:
        #'.'点是从当前标签开始的
        house_name_title = house_name.xpath('./div[2]/h2/a/text()')[0]
        #在文件写入时，不能在后面添加参数
        fp.write(house_name_title+'\n')
        print(house_name_title+ '写入成功')