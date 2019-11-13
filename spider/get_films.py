#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   get_films.py    
@Contact :   18360979676@qq.com
@License :   (C)Copyright 2016-2019

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/19 20:45   yezhu      1.0         None
--------------------- 
"""
import urllib.request
import re
import time, random
from bs4 import BeautifulSoup


class GetFilms(object):
    def __init__(self):
        self.base_url = 'https://www.dytt8.net'
        self.url = "https://www.dytt8.net/html/gndy/dyzz/index.html"
        self.user_agents = [('User-Agent', 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'), ]
        self.headers = [random.choice(self.user_agents), ("Connection", "keep-alive")]
        # 构建opener
        self.http_handler = urllib.request.HTTPHandler(debuglevel=1)
        self.opener = urllib.request.build_opener(self.http_handler)
        # 添加请求头
        self.opener.addheaders = self.headers

    def get_pagnum(self):
        data = self.opener.open(self.url).read()
        res = re.findall(r'list\_23\_[0-9]*', str(data))
        if res:
            page_num = res[-1].split("_")[-1]
            print('获取到页码数%s' % page_num)

            return int(page_num) if int(page_num) < 4 else 4

    def find_by_page(self, page=1):
        if page % 10 == 0:
            time.sleep(random.randint(1, 3))
        urls = "https://www.dytt8.net/html/gndy/dyzz/list_23_%s.html" % (str(page))
        data = self.opener.open(urls).read()
        res = re.findall(r'class\=\"co\_content8\"[\s\S]*\<\/ul\>', str(data))[0]
        # res = re.findall(r'\/html\/gndy\/dyzz\/[0-9]{1, }\/[0-9]{1, }\.html', str(res))
        res = BeautifulSoup(str(res), 'html5lib')
        res = res.find_all('a', class_='ulink')
        urls = [self.base_url + temp_url['href'] for temp_url in res]
        print('爬取第%s页:' % page)
        return urls

    def get_urls(self, pages=1):
        all_urls = []
        for page in range(1, pages + 1):
            for r in self.find_by_page(page):
                all_urls.append(r)
        print('获取到%s条链接' % len(all_urls))
        return all_urls


if __name__ == '__main__':
    get_urls = GetFilms()
    out = '\n'.join(get_urls.get_urls(get_urls.get_pagnum()))  # 获取到所有的超链接列表
    with open('../publicFile/img/get_films/all_urls.txt', 'a') as f:
        f.write(out)
