# -*- encoding: utf-8 -*-
'''
@File    :   WallPaper.py
@Time    :   2020/04/25 17:57:00
@Author  :   Liu Qidong
@Version :   1.0
@Contact :   dong_liuqi@163.com
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup as bs
import re

main_url = 'http://www.netbian.com'    #爬取背景的网站
save_path = 'H:/DesktopBackground/'


def Get_calendar(year=2020, month=6, img_num=5):
    url = main_url + '/rili/'
    save_path = r'G:/DesktopBackground/'
    match_date = str(year) + '年' + str(month) + '月'

    r = requests.get(url, timeout=10)    #链接到日历的主页面，在这里面寻找所有符合的图片
    r.encoding = 'gbk'    #编码要是gbk，负责中文无法识别
    soup = bs(r.text,'html.parser')    #用bs库把网页代码整成标签数

    #获取当月日历壁纸的url列表
    url_list = []
    tag_list = soup.find_all('a')    #找到全部的a标签
    for tag in tag_list:
        if tag.get('title') is not None:    #需要判断a标签里的title是否为空，负责可能会报错
            temp = re.search(match_date, tag.get('title'))    #img标签里的alt如果含有目标年月，就下载
            if re.search(match_date, tag.get('title')):
                make_url = tag.get('href').split('.')[0] + '-1920x1080.htm'    #直接去到1920x1080分辨率的背景的网页
                url_list.append(tag.get('href'))    #把含有目标背景图的url找到

    #将列表中的图片都下载下来
    if len(url_list) < 5:
        img_num = len(url_list)    #如果网页中能找到的图的数量小于输入的数量

    for i in range(img_num):
        r = requests.get((main_url + url_list[i]), timeout=10)
        r.encoding = 'gbk'
        soup = bs(r.text, 'html.parser')
        tag_list = soup.find_all('img')    #直接去找img标签，目标图的url就在这个标签里
        for tag in tag_list:
            if tag.get('title') is not None:
                if re.search(match_date, tag.get('title')):
                    url = tag.get('src')
        r = requests.get(url, timeout=10)
        write_path = save_path + str(year) + str(month) + '0' + str(i) + '.jpg'
        with open(write_path, 'w+b') as f:
            f.write(r.content)
    

    return 0


def Delete_All():

    return 0


if __name__ == '__main__':
    Get_calendar()

    print('Mission Complete!')

