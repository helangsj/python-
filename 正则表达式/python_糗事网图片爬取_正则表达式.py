import requests
import re
import os
if __name__ == "__main__":
    #1、请求的url地址
    url = "https://www.qiushibaike.com/8hr/page/%d/"
    #设置请求头，用于检测浏览器识别
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    #文件夹判断
    if not os.path.exists("./qiushiImg"):
        os.makedirs("qiushiImg")
    for page_num in range(1,5):
        new_url = format(url%page_num)
        print(new_url+"第%d页数据"%page_num)
        #设置首页请求数据
        response = requests.get(url=new_url,headers=headers).text
        #设置正则表达式，在使用正则表达式的时候需要注意提取的值
        ex = '<a class="recmd-left image".*?>.*?<img src="(.*?)" alt.*?</a>'
        #使用正则表达式寻找相关的数据，其中re.S
        exec = re.findall(ex,response,re.S)
        # 修饰符	描述
        # re.I	使匹配对大小写不敏感
        # re.L	做本地化识别（locale-aware）匹配
        # re.M	多行匹配，影响 ^ 和 $
        # re.S	使 . 匹配包括换行在内的所有字符
        # re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
        # re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

        #exec ['//pic.qiushibaike.com/system/pictures/12395/123956724/small/ESUAC13DR5D7ZXND.jpg?imageView2/1/w/150/h/112']地址，还差https协议
        for img_url in exec:
            img_url = "https:" + img_url
            #请求图片,由于图片是二进制的，所以需要content类型
            img_response =  requests.get(url=img_url,headers=headers).content
            img_name = img_url.split('?')[-2].split('/')[-1]
            img_path = "./qiushiImg/" + img_name
            #存储二进制文件时使用‘wb’，不能使用编码utf-8编码，在这里犯了前面json数据的一个错误
            with open(img_path,'wb') as fp:
                fp.write(img_response)