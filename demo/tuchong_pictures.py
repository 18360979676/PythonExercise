#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   TuChong_pictures.py    
@Contact :   18360979676@qq.com
@License :   (C)Copyright 2016-2019

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/9 1:21   yezhu      1.0         None
--------------------- 
"""

import requests, urllib3, json, time, os
from contextlib import closing
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class TuChong(object):
    """
    构造函数
    """
    def __init__(self, download_server):
        self.photo_url = []
        self.top_url = 'http:'
        self.download_server = download_server

    """
    获取图片地址
    """
    def get_urls(self):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'X-Requested - With': 'XMLHttpRequest',
            'Host': 'www.ly.com',
            'Referer': 'https://www.ly.com/youlun/',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }
        data = {
            'Type': 'GetHomePageSellingPower',
            'specialId': 693,
            'moduleIds': 1454,
            'pageSize': 4,
            'cityId': 226
        }
        req = requests.get(url=self.download_server, params=data, verify=False, headers=headers)
        html = json.loads(req.text)
        for each in html['Data']:
            self.photo_url.append(self.top_url + each['StlImageUrl'])
        time.sleep(1)

    """
    图片下载
    """
    def download(self, photo_url, filename):
        with closing(requests.get(url=photo_url, stream=True, verify=False)) as r:
            start_time = datetime.now()
            with open('../publicFile/img/TuChong/%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
            end_time = datetime.now()
            sec = (end_time - start_time).microseconds
            print('下载耗时{0}us'.format(sec))


def tick():
    tc = TuChong('https://www.ly.com/youlun/AjaxCruiseActivity.aspx')
    print('获取图片链接中：')
    tc.get_urls()
    print('图片下载中：')
    for i in range(len(tc.photo_url)):
        print('正在下载第%d图片' % (i + 1))
        tc.download(tc.photo_url[i], (i + 1))
    print('下载完成')


if __name__ == '__main__':
    # scheduler = BlockingScheduler()
    # # scheduler.add_job(tick, 'interval', seconds=10)  # 时间间隔触发抓包
    # scheduler.add_job(tick, 'cron', hour=16, minute=31, second=41)  # 这里表示每天的19：28 分执行任务。这里可以填写数字，也可以填写字符串
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     pass
    tick()
