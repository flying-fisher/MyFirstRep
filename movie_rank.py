# -*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import lxml
import time
import json

headers = {'Referer':'http://www.cbooo.cn/p/2247344',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

urls = ['http://www.cbooo.cn/Mdata/getMdata_movie?area=50&type=0&year=0&initial=%E5%85%A8%E9%83%A8&pIndex={}'.format(str(i)) for i in range(1,346+1)]
for url in urls[:1]:
    #print(url)
    response = requests.get(url,headers = headers)
    html = response.text
    #print('pData' in html)
    html1 = eval(html)
    print(type(html1))
    items = html1['pData']
    #print(MovieName)
    for item in items:
        data = {
            'MovieName' : item['MovieName'],
            'id ': item['BoxOffice'],
             'rank ':item['Ranking'],
            'generate_year' : item['releaseYear'],
            'image' : item['defaultImage']
        }


        id = 'http://www.cbooo.cn/m/' + data['id ']
        #print(id)
        id_response = requests.get(id,headers = headers).text
        print(id_response)
        soup1 = BeautifulSoup(id_response,'lxml')
        actors_group = soup1.find('div',{'class':'starring'})
        actor_group = actors_group.find_all('li')
        for actor in actor_group:
            name = actor.a['title']
            #state = actor.p[0].get_text
            #generate_data = actor.p[1].get_text
            print(name)




        '''
        print(json.dumps(data,ensure_ascii=False))
        with open('dianying.json','a',encoding='utf-8') as f:
            f.write(json.dumps(data,ensure_ascii=False) + '\n')

        
        MovieName = item['MovieName']
        id = item['BoxOffice']
        rank = item['Ranking']
        generate_year = item['releaseYear']
        image = item['defaultImage']
        print(MovieName,'  ',id)
        '''