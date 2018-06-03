# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import urllib

class VOA_spider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        self.url = 'http://www.51voa.com/Technology_Report_1.html'
        self.name = []
        self.urls = []
        self.musics = []

    def get_content_url(self):
        response = requests.get(self.url,headers = self.headers)
        pattern = re.compile('<div id="list"><ul>(.*?)</ul></div>',re.S)
        html = re.findall(pattern,response.text)
        pattern1 = re.compile('<a href="(.*?)" target=_blank>(.*?)</a>',re.S)
        html1 = re.findall(pattern1,html[0])
        return html1

    def parse_content(self,url):
        #print(url)
        response = requests.get(url,headers = self.headers)
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        content = soup.find_all('div',{'id':'content'})
        content_all = BeautifulSoup(str(content[0]),'lxml')
        p_s = content_all.find_all('p')
        #author = content_all.find('span',_class='byline')
        #datetime = content_all.find('span',_class='datetime')
        items = []
        for p in p_s:
            content_c = p.text.replace('<strong>', '')
            content1 = content_c.replace('â', '---')
            items.append(content1)
        #print(items)
            #print(content1)
        return items
        #return items




    def get_music(self,url):
        response = requests.get(url,headers = self.headers)
        html = response.text
        pattern = re.compile('<a id="mp3" href="(.*?)"></a>',re.S)
        music = re.findall(pattern,html)
        #print(music[0])
        return music[0]

    def save_article_content(self,content,name):
        #path = 'E:\\pycharm\\data/English_voa/article/'
        with open('E:/pycharm/data/English_voa/article/{}.txt'.format(str(i) for i in range(

        )),'w',encoding='utf-8') as f:
            f.writelines(content)
            f.write('\n\n')

    def save_article_mp3(self,name,music):
        urllib.request.urlretrieve(music,'E:\\pycharm\\data/English_voa/article_mp3/'+ str(name) + '.mp3')

    def runs(self):
        # 1.输入网页url
        html_list = self.get_content_url()
        print(len(html_list))
        for link in html_list[:1]:
            self.urls.append('http://www.51voa.com'+ link[0])
            self.name.append(link[1])
            url = 'http://www.51voa.com' + link[0]
            name = link[1].replace('?','_')
            #print(name)
            # 2.解析网页  # 3.获取内容
            content = self.parse_content(url)
            #print(list(content))
            music = self.get_music(url)
            #print(music,name,content)
            #self.save_article_content(content,name)
            #self.save_article_mp3(name,music)
            print("保存成功！")

        # 4.保存数据内容
if __name__ == '__main__':
    VOA_download_content = VOA_spider()
    VOA_download_content.runs()