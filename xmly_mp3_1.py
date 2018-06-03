# -*- coding:utf-8 -*-


# 导入第三方库函数
import requests
from bs4 import BeautifulSoup
import urllib

# 网页头文件
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


def get_url():
    pass


def parse_url():    #解析网页，找出每个mp3音频文件链接的项目
    urls = ['http://www.ximalaya.com/waiyu/yingyu/4323746/p{}/'.format(str(pn)) for pn in range(1, 10)]
    for url in urls:
        print(url)
        data = []
        response = requests.get(url, headers=headers)
        source_html = response.text
        soup = BeautifulSoup(source_html, 'lxml')
        items = soup.find_all('li', {'class': 'e-2304105070'})
        data.append(items)
    return data


def parse_item(item): #通过每个item,获得音频文件

    href = 'www.ximalaya.com' + item.a['href']
    name = item.a.text.strip()
    id = href.split('/')[-1]  # 首先切片划分，然后取出最后面的ID号
    # 经过网页分析可以这样进行书写
    mp3_url = 'http://www.ximalaya.com/revision/play/tracks?trackIds=' + id
    resp = requests.get(mp3_url, headers=headers).json()
    mp3 = resp['data']['tracksForAudioPlay'][0]['src']
    return mp3,name


def download_mp3(mp3,name):
    try:
        urllib.request.urlretrieve(mp3, 'E:\\music\\' + str(i) + str(name) + '.mp3')

        print('下载完成', name)

    except:
        urllib.request.urlretrieve(mp3, 'E:\\music\\' + str(i) + str(name[:14]) + '.mp3')
        print('名称里有特殊字符')


def fun():
    sounds = parse_url()
    for item in sounds:

        for mp3,name in parse_url(item):
            download_mp3(mp3,name)


if __name__ == '__main__':
    fun()