# -*- coding: utf-8 -*-
#爬取百度图片

from urllib.request import *
# 用来处理网络访问
import re
import time

# 访问网络开始时间
start_time = time.time()
url = 'https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&tab=album'
html = urlopen(url) # 用来打开一个网页
# html代码
obj = html.read().decode()

#获取html代码并解码
urls = re.findall(r'<img src="(.*?.jpg)"',obj) #.>列表
#非贪婪（.*?）
index = 0
path = 'e:\picture\\'
for url in urls:
    print('download...%d'%index)
    urlretrieve(url,path+'pic'+ str(index)+'.jpg')
    index += 1

