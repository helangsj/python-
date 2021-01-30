#代理IP应用
import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://www.ipip.net/'
    headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.88Safari / 537.36'
    }
    response = requests.get(url=url,headers=headers,proxies={"https":"123.55.98.193:9999"}).text
    # q = response.content
    print(response)
    tree = etree.HTML(response)
    q = tree.xpath('//html/body/div[1]/center/text()')
    print(q)