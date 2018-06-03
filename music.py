# -*- coding:utf-8 -*-

import requests
import re

url = 'http://www.51voa.com/VOA_Special_English/scientists-early-humans-were-not-as-simple-as-one-would-think-78505.html'
response  = requests.get(url)
html = response.text
pattern = re.compile('<a id="mp3" href="(.*?)"></a>',re.S)
music = re.findall(pattern,html)
print(music[0])