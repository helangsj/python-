import requests
import json

if __name__ == "__main__":
    #1、请求地址
    url = 'https://fanyi.baidu.com/sug'
    # UA防伪
    headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    #输入单词动态化
    word = input("请输入单词：")
    # 3、请求数据
    data = {
        'kw':word
    }
    # 4、在抓包工具中可以看出是get或post请求
    response = requests.post(url=url,data=data,headers=headers)
    # 在工具中可以看出返回的类型属于什么类型，其中返回的是json类型，才能使用json对象
    obj = response.json()
    #4、数据持久化存储
    filename = word+'.json'
    fp = open(filename,'w',encoding='utf-8')
    #json文件存储，其中有中文，中文不能使用ascii码解，所以设置为false
    json.dump(obj,fp,ensure_ascii=False)
    print("破解百度翻译结束!!")

'''
学习终结:
    1、json文件存储方法json.dump()
    2、中文ascii编码不能解中文
    3、文件写入open()
'''