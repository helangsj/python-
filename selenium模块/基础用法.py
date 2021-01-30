from selenium import  webdriver
from lxml import etree

#实例化一个浏览器对象（传入浏览器驱动）
bro = webdriver.Chrome(executable_path='./chromedriver')
#让浏览器对一个指定的url指定请求
bro.get(url=url)
#使用page_source来获取当前页面的源码数据
page_text = bro.page_source
#使用etree解析数据
etree.HTML(page_text)
#关闭浏览器
bro.quit()

