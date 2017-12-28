#-*- coding:utf-8 -*-
import requests,time
from bs4 import BeautifulSoup


class download_stories(object):
    def __init__(self):
        self.server = 'http://www.17k.com/'
        self.target = 'http://www.17k.com/list/2065918.html'
        self.name = []
        self.urls = []
        self.num = 0

    def get_download_urls(self):
        url = self.target
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        div_s = soup.find_all('dl', class_='Volume')
        #print(div_s[1:])
        a_bf = BeautifulSoup(str(div_s[1:]), 'lxml')
        a_s = a_bf.find_all('a')

        self.num = len(a_s[1:51])

        for a in a_s[1:51]:
            self.name.append(a.text)
            self.urls.append(self.server + a.get('href'))


    def get_content(self, target):
        html = requests.get(target).text
        soup = BeautifulSoup(html, 'lxml')
        texts = soup.find_all('div', class_='p')
        content = texts[0].text.replace(' '*2,'')
        return content

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    u1 = download_stories()
    u1.get_download_urls()
    print("《参天》开始下载：")
    for i in range(u1.num):
        u1.writer(u1.name[i], 'e:\\scrapy_data\参天.txt', u1.get_content(u1.urls[i]))
    print("下载完毕\n")