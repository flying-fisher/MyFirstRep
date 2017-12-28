#-*- coding:utf-8 -*-

import requests,sys
from bs4 import BeautifulSoup
import time

class downloader(object):

    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/24_24286/'
        self.name = []     #存放章节名
        self.urls = []     #存放章节链接
        self.nums = 0      #章节数

    def get_download_url(self):
        url = requests.get(self.target)
        html = url.text
        soup = BeautifulSoup(html,'lxml')
        div = soup.find_all('div',class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]),'lxml')
        a = a_bf.find_all('a')
        self.nums = len(a[12:])        #删除不必要的章节，并统计
        for each in a[12:]:
            self.name.append(each.text)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self,target):
        req = requests.get(target)
        html = req.text
        bf = BeautifulSoup(html,'lxml')
        texts = bf.find_all('div',class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding = 'utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print('《超级侦探》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.name[i],'e:\\scrapy_data\超级侦探.txt',dl.get_contents(dl.urls[i]))
    print('《超级侦探》下载完毕')