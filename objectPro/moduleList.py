#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'lyl'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('一个参数也没有')
    else:
        print(args)


if __name__ == '__main__':
    test()


# 封装函数的内部逻辑


def _private_1(name):
    return 'hello, %s' % name


def _private_2(name):
    return 'hi, %s' % name


def greeting(name):
    if len(name) > 3:
        _private_1(name)  # 调用第1个
    else:
        _private_2(name)  # 调用第2个
