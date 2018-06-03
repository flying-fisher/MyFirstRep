# -*- coding:utf-8 -*-
import requests
import json
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'.format(str(i*20)) for i in range(0,10)]
for url in urls:
    #print(html)
    response = requests.get(url,headers = headers)
    html = response.text
    result=json.loads(html)
    tvs = result['subjects']
    tv_list = []
    for i in range(0,len(tvs)):

        tv = {}
        tv['rate'] = tvs[i]['rate']
        tv['title'] = tvs[i]['title']
        tv['cover'] = tvs[i]['cover']
        tv['url'] = tvs[i]['url']
        tv['id'] = tvs[i]['id']
        #print(tv)
        tv_list.append(tv)
    print(tv_list)


