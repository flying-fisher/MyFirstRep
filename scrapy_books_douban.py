# -*- coding: utf-8 -*-
#豆瓣励志书籍

import requests
import re
import time
start = time.time()
contents = requests.get('https://book.douban.com/latest?icn=index-latestbook-all').text
pattern = re.compile('<li.*?detail-frame.*?href=.*?>(.*?)</a>.*?color-gray">(.*?)</p>',re.S)

resulta = re.findall(pattern,contents)
print(resulta)
for resultas in resulta:
    name,year = resultas
    year = re.sub('\s','',year)
    print(name,year)
    time.sleep(1)
end = time.time()
time = end - start
print(time)