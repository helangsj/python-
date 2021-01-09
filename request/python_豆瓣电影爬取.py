import requests
import json
if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list'
    pagrams = {
    'type': '24',
    'interval_id': '100:90',
    'action':'',
    'start': 0,
    'limit': 20
    }
    headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response =  requests.get(url=url,params=pagrams,headers=headers)
    list_douban = response.json()
    filename = './douban.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(list_douban,fp=fp,ensure_ascii=False)
    print("爬取结束")