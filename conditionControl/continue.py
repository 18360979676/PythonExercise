#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/7/12 20:03
#@Author: yezhu
#@File  : continue.py
import sys
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        #循环中没有找到元素
        print(n, '是质数')
print(sys.path)