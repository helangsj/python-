from selenium import  webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://qzone.qq.com/')
#获取iframe标签
bro.switch_to.frame('login_frame')
#获取iframe标签下的使用密码账号登录
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

#获取用户框
username = bro.find_element_by_id('u')
#获取密码
password = bro.find_element_by_id('p')
sleep(1)
#使用send_keys方法写入
username.send_keys('1729625382')
sleep(1)
password.send_keys('413765934062.')
sleep(1)
clic_btn = bro.find_element_by_id('login_button')
clic_btn.click()
sleep(3)
bro.quit()