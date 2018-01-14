# -*- coding: utf-8 -*-
#抓取百度贴吧---生活大爆炸吧的基本内容
#爬虫线路： requests - bs4
#Python版本 : 3.5.1
#http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8&pn=0
'''
# 一个大的li标签内包裹着很多个div标签，而我们要的信息就在这一个个div标签之内：

# 标题&帖子链接：
<a href="/p/4830198616" title="又重温一遍 第九季  这个侧脸给多少分" target="_blank" class="j_th_tit ">又重温一遍 第九季  这个侧脸给多少分</a>

#发帖人：
<span class="tb_icon_author " title="主题作者: Li欣远" data-field='{&quot;user_id&quot;:836897637}'><i class="icon_author"></i><span class="frs-author-name-wrap"><a data-field='{&quot;un&quot;:&quot;Li\u6b23\u8fdc&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=Li%E6%AC%A3%E8%BF%9C&ie=utf-8&fr=frs" target="_blank">Li欣远</a></span>

#回复数量：
<div class="col2_left j_threadlist_li_left">
<span class="threadlist_rep_num center_text" title="回复">24</span>
</div>

#发帖日期：
 <span class="pull-right is_show_create_time" title="创建时间">2016-10</span>
'''

import requests
from bs4 import BeautifulSoup
import time

#首先我们写好抓取网页的函数

def get_html(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        #贴吧编码是utf-8。爬取其他的页面时建议使用：
        #r.encoding = r.apparent_encoding
        r.encoding = 'utf-8'
        return r.text
    except:
        return "Error"

def get_content(url):
    '''
    分析贴吧的网页文件，整理信息，保存在列表变量中
    :param url:
    :return:
    '''
    # 初始化一个列表来保存所有的帖子信息：
    comments = []
    #首先，我们把需要爬取信息的网页下载到本地
    html = get_html(url)

    # 我们来做一锅汤
    soup = BeautifulSoup(html,'lxml')

    # 按照之前的分析，我们找到所有具有‘ j_thread_list clearfix’属性的li标签。返回一个列表类型。
    liTags = soup.find_all('li',attrs = {'class':'j_thread_list clearfix'})

    for li in liTags:
        # 初始化一个字典来储存文章信息
        comment = {}
        # 这里使用一个try except 防止爬虫找不到信息从而停止运行
        try:
            #开始筛选信息，并保存到字典中
            comment['title'] = li.find('a',attrs = {'class':'j_th_tit'}).text.strip()
            print()
            comment['link']  = "http://tieba.baidu.com/" + li.find('a',attrs = {'class':'j_th_tit'})['href']
            comment['name']  = li.find('a',attrs = {'class':'tb_icon_author'})['title']
            comment['time']  = li.find('span',attrs = {'class':'pull-right is_show_creat_time'})['title'] + li.find('span',attrs = {'class':'pull-right is_show_creat_time'}).text.strip()
            comment['replyNum'] = li.find('span',attrs = {'class':'threadlist_title'}).text.strip()
            comments.append(comment)
            print(comment)

        except:
            print('出了点小问题')

    print(comments)
    return comments

def Out_to_File(dict):
    '''
    将爬取到文件写入到本地
    保存到当前目录的TTBT.txt文件中。
    :param dict:
    :return:
    '''
    with open('e:\TTBT.txt','a+') as f:

        for comment in dict:
            f.write('标题：{} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量：{} \n'.format(comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))

        print('当前页面爬取完成')

def main(base_url,deep):
    url_list = []
    # 将所有需要爬取的url存入列表
    for i in range(0,deep):
        url_list.append(base_url + '&pn=' + str(50*i))
    print('所有的网页已经下载到本地！ 开始筛选信息。。。。')

    #循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        Out_to_File(content)
    print('所有的信息都已经保存完毕！')

base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
deep = 3

if __name__ == '__main__':
    main(base_url,deep)