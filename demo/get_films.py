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


class GetFilms(object):
    def __init__(self):
        self.base_url = 'http://www.ygdy8.com'
        self.url = "http://www.ygdy.com/html/gndy/dyzz/index"
        self.user_agents = [('User-Agent', 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'), ]
        self.headers = [random.choice(self.user_agents), ("Connection", "keep-alive")]
        # 构建opener
        self.opener = urllib.request.build_opener()
        # 添加请求头
        self.opener.addheaders = self.headers

    def get_pagnum(self):
        data = self.opener.open(self.url).read()
        res = re.findall(r'list\_23\_[0-9]*', str(data))
        if res:
            page_num = res[-1].split("_")[-1]
            print('获取到页码数%s' % page_num)
            return int(page_num)

    def find_by_page(self, page=1):
        if page % 10 == 0:
            time.sleep(random.randint(1, 3))
        urls = "http://www.ygdy8.com/html/gndy/dyzz/list_23_%s.html" % (str(page))
        data = self.opener.open(urls).read()
        res = re.findall(r'class\=\"co\_content8\"[\s\S]*\<\/ul\>', str(data))[0]
        res = re.findall(r'\/html\/gndy[/a-z]+[0-9/]{1, }\.html', str(res))
        urls = [self.base_url + temp_url for temp_url in res]
        print('爬取第%s页:' % page + str(urls))
        return urls

    def get_urls(self, pages=1):
        all_urls = []
        for page in range(1, pages + 1):
            for r in self.find_by_page(page):
                all_urls.append(r)
        all_urls = set(all_urls)
        print('获取到%s条链接' % len(all_urls))
        return all_urls


if __name__ == '__main__':
    out = ''
    get_urls = GetFilms()
    for url in get_urls.get_urls(get_urls.get_pagnum()):
        url = str(url) + '\n'
        out = out + url
    with open('../publicFile/img/get_films/all_urls.txt', 'w') as f:
        f.write(out)
