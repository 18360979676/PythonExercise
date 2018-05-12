#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'

from datetime import datetime, timedelta
from collections import Counter

now_time = datetime.now()
# print('当前时间：', now_time)
# print('时间变量类型：', type(now_time))


dt = datetime(2018, 5, 11, 13, 12, 00)
# print(dt)  # 用指定日期时间创建datetime
# print(dt.timestamp())  # 返回当前时间对应的秒数单位


# 时间字符串格式转换为datetime对象
# print(datetime.strptime('2018-05-11 13:29:00', '%Y-%m-%d %H:%M:%S'))


# datetime对象转换为str字符串模式
now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))


# 对datetime对象加减
# print(now + timedelta(hours=10))  # 加10小时
# print(now + timedelta(days=1))  # 加1天


# 统计字符出现的次数
c = Counter()
for ch in 'lyl123':
    c[ch] = c[ch] + 1;
print(c)
