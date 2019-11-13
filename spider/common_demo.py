#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   temp_demo.py    
@Contact :   18360979676@qq.com
@License :   (C)Copyright 2016-2019

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/20 21:12   yezhu      1.0         None
--------------------- 
"""
import urllib.request
import random
url = 'https://www.dytt8.net/html/gndy/dyzz/index.html'
user_agent_list = ['Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50', 'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1', 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36']
headers = {
    'User-Agent': random.choice(user_agent_list)
}
opener = urllib.request.build_opener()
request = urllib.request.Request(url, headers=headers)
response = opener.open(request)
print(response.read())
