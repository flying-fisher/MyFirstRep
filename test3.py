import requests
import re

contents = requests.get("https://book.douban.com/latest?icn=index-latestbook-all").text




pattern = re.compile('<li.*?detail-frame.*?href.*?>(.*?)</a>.*?color-gray">(.*?)<\p>',re.S)
resulta = re.findall(pattern,contents)


for resultas in resulta:
    book_name,author = resultas
    author = re.sub('\s','',author)
    print("<<"+book_name+">>",author)