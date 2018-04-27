#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'


# 使用元类
# 可以使用type()函数创建新的类型
def fn(self, name = 'world'):
    print('Hello, %s' % name)


Hello = type('Hello', (object, ), dict(hello = fn))  # 创建Hello class
h = Hello()
print('Hello类型是:', type(Hello))
print('类的实例对象类型是:', type(h))
