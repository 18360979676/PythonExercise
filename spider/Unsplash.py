#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Unsplash.py    
@Contact :   18360979676@qq.com
@License :   (C)Copyright 2016-2019

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/7 14:16   yezhu      1.0         None
--------------------- 
"""

import requests, urllib3, json, time, sys
from contextlib import closing

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class get_youluns(object):
    """
    构造函数
    """
    def __init__(self):
        self.photo_url = []
        self.download_server = 'https://www.ly.com/youlun/AjaxCruiseActivity.aspx?Type=GetHomePageSellingPower&specialId=693&moduleIds=1454&pageSize=4&cityId=226'

    """
    获取图片地址
    """
    def get_urls(self):
        req = requests.get(url=self.download_server, verify=False)
        html = json.loads(req.text)
        for each in html['Data']:
            self.photo_url.append(each['StlImageUrl'])
        time.sleep(1)

    """
    图片下载
    """
    def download(self, photo_url, filename):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        target = 'http:' + photo_url
        with closing(requests.get(url=target, stream=True, verify=False, headers=headers)) as r:
            with open('../publicFile/img/Unsplash/%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == '__main__':
    gy = get_youluns()
    print('获取图片链接中：')
    gy.get_urls()
    print("图片下载中:")
    for i in range(len(gy.photo_url)):
        print('正在下载第%d图片' % (i + 1))
        gy.download(gy.photo_url[i], (i + 1))
    print('下载完成')




