#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'


import hashlib, itertools
# 计算元素的哈希值
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('pythonhashlib '.encode('utf-8'))
# print(md5.hexdigest())

# 迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c:c.upper()):
    print(key, list(group))

