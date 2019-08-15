# -*- coding:gbk -*-
__author__ = 'Administrator'
# 'Administrator' 为预定义的变量，为你当前登录的计算机用户名

from bs4 import BeautifulSoup

import requests, sys

"""
类说明:下载《笔趣看》网小说《一念永恒》
"""


class DownLoader(object):
    """
    构造函数
    """
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []  # 存放章节名
        self.urls = []   # 存放章节链接
        self.nums = []   # 章节数
    """
    函数说明：获取下载链接
    """
    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding = 'gbk'  # 指定网页编码类型
        html = req.text()
        div_bf = BeautifulSoup(html, "html5lib")
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]), "html5lib")
        a = a_bf.find_all('a')
        self.nums = len(a[16:])
        for each in a[16:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    """
    函数说明：获取章节内容
    """
    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = 'gbk'  # 指定网页编码类型
        html = req.text
        bf = BeautifulSoup(html, "html5lib")
        texts = bf.find_all('div', class_='showtxt')
        texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        return texts

    """
    函数说明:将爬取的文章内容写入文件
    """
    def writer(self, name, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = DownLoader()
    dl.get_download_url()
    print('《一念永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '../publicFile/一念永恒.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("已下载:%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一念永恒》下载完成')
