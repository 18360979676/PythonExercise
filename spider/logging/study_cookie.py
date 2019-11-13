#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   study_cookie.py    
@Contact :   18360979676@qq.com
@License :   (C)Copyright 2016-2019

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/22 8:54   yezhu      1.0         None
--------------------- 
"""
import urllib.request
import ssl
from urllib.parse import urlencode


def test():
    try:
        import cookielib
    except:
        import http.cookiejar as cookielib

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    cookie = cookielib.CookieJar()
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cookie_handler)
    headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')]
    opener.addheaders = headers
    target_url = 'http://www.renren.com/PLogin.do'
    data = {'email': '18360979676', 'password': 'lyl123'}
    data = urlencode(data).encode('utf-8')
    request = urllib.request.Request(target_url, data=data)
    result_response = opener.open(request)  # 首次访问页面，复制cookie对象;
    result_response = opener.open('http://www.renren.com/972008280/newsfeed/specialfocus')  # opner已有cookie对象去访问其它页面(免登录)
    print(result_response.read().decode('utf-8'))


if __name__ == '__main__':
    test()
