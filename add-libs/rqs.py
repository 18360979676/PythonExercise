#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'

import requests, json
# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})  # 豆瓣主页
# print('状态码:', r.status_code, '\n内容:', r.text)
# print('实际请求的url', r.url)


r = requests.get('https://api.github.com/user', auth=('18360979676@163.com', 'querenmima123,./'))
jsTxt = r.json()
for item in r.json():
    print('%s: %s' % (item, jsTxt[item]))
print(r.url)

