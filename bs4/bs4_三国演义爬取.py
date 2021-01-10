import  requests
import lxml
import os
#需求爬取三国演义的所有章节
from bs4 import BeautifulSoup
if __name__ == "__main__":
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
   #创建小说存储地址
    if not os.path.exists('./小说'):
        os.makedirs('./小说')
    #开始页数据请求
    response = requests.get(url=url,headers=headers).text
    #使用bs4解析
    soup = BeautifulSoup(response,'lxml')
    #查找各章节的li标签
    list_all_chapter = soup.select('.book-mulu > ul > li')
    fp = open("./小说/三国演义.text",'w',encoding='utf-8')
    #爬取每个章节页
    for list_everyList in list_all_chapter:
        #章节名称
        chapter_name = list_everyList.get_text()
        #章节详情地址
        list_href = "https://www.shicimingju.com"+ list_everyList.a['href']
        #请求章节详情地址
        chapter_details_response = requests.get(url=list_href,headers=headers).text

        chapter_details_soup = BeautifulSoup(chapter_details_response,'lxml')
        #章节详情
        chapter_details_text = chapter_details_soup.find('div',class_='chapter_content').text
        fp.write(chapter_name + ":"+ chapter_details_text + "\n" )
        print(chapter_name + "爬取成功")