from selenium import  webdriver
from time import sleep
#导入无可视化界面模块
from selenium.webdriver.chrome.options import Options
#s实现规避检测
from selenium.webdriver import  ChromeOptions

#无头浏览器设置
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#如何实现selenium规避被检测到的风险
options =ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-automation'])

#在浏览器驱动中加入无头浏览器设置参数
bro = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options,options=options)
#无可视化界面（无头浏览器）
bro.get('https://www.baidu.com')
#打印页面信息
print(bro.page_source)
sleep(2)
#关闭浏览器
bro.quit()