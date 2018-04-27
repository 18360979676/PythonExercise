#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'

# 记录错误的调用堆栈
import logging


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


def bar(s):
    return foo(s) * 2


def main():

    bar('0')


main()
print('END')
