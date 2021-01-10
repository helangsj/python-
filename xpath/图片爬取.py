import requests
from lxml import etree
import  os

if __name__ == "__main__":
    #彼岸图网网址
    url = 'http://pic.netbian.com/4kfengjing/'
    headers = {'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.88Safari / 537.36'}
    response = requests.get(url=url,headers=headers)
    response.encode='utf-8'
    tree = etree.HTML(response.text)
    all_li = tree.xpath('//div[@class="slist"]/ul/li')
    if not os.path.exists('./tupian'):
        os.makedirs('tupian')
    for li_img in all_li:
        # "http://pic.netbian.com" +
        img_url =  "http://pic.netbian.com" + li_img.xpath('./a/img/@src')[0]
        img_name = li_img.xpath('./a/img/@alt')[0]
        #解决乱码问题
        img_name = img_name.encode('iso-8859-1').decode('gbk')+ '.jpg'
        path ='./tupian/' + img_name
        #重新请求下载图片
        img_downd = requests.get(img_url,headers=headers).content
        with open(path,'wb') as fp:
            fp.write(img_downd)
            print( img_name +'下载成功')


