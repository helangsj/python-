#目的：
    #爬取改网站的目的是为了练习使用xpath进行页面解析时，可以使用 | 或符号
import  requests
from lxml import etree

if __name__ == "__main__":
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.88Safari / 537.36'}
    reponse = requests.get(url,headers=headers).text
    tree = etree.HTML(reponse)
    #按照流程来做的话，这里时热门城市和全国城市分开解析，分开亲求
    # 2、这里使用另外一种方法，使用| 运算符
    all_city = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
    all_cities = []
    for city in all_city:
        a_city = city.xpath('./a/text()')[0]
        all_cities.append(a_city)
    print(all_cities,len(all_cities))