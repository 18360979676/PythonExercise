#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
import time

# 函数式编程
# 高阶函数--一个函数接收另一个函数作为参数
# 函数名是指向函数的变量


def add(x, y, fn):
    return fn(x) + y

# map高阶函数
# 字符串转换为整数--lambda优化一下函数
# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2Int(s):
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# print(str2Int("5656"))

# 英文名字首字母大写
# nameStr = ['dfdK  dfddf', 'TjjjT']
def normalize(name):
    return name.capitalize()
# print(list(map(normalize, nameStr)))

# filter高阶函数


def is_odd(n):
    # 删除偶数，保留奇数
    return n % 2 == 1
# print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

# 删除序列的空字符串


def not_empty(s):
    return s and s.strip('d')
# print(list(filter(not_empty, ['a', '', 'b', 'dddfd    ds  '])))


# 高阶函数sorted升序排序-----
# ------ reverse=True选项 ------
# 忽略字符串大小写进行排序
# print(sorted(['adfd', 'bdfd', 'Fjj', 'Credit'], key=str.lower))

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sort_name(bTple):
    return bTple[1]
# print(sorted(L, key=sort_name, reverse=True))

# 匿名函数
# R = list(filter(lambda n: n%2 == 1, range(1, 20)))
# print(R)


# 装饰器--在函数运行之前执行一些任务

# 公共文件内容区
def content(s, arg):
    @functools.wraps(arg)
    def wrapper(*args, **kw):
        print(s)
        print('begin call')
        r = arg(*args, **kw)
        print('end call')
        return r
    return wrapper


def log(arg):
    if not isinstance(arg, str):
        return content('不带参数列表', arg)
    else:
        def decorator(func):
            return content('带参数列表', func)

        return decorator

# 函数运行之前，打印函数日志


@log
# @log('123')
def now():
    print('2018-04-26')


now()


def performance(f):  # 打印出函数执行的时间
    def fn(*args, **kw):
        t_start = time.time()
        r = f(*args, **kw)
        t_end = time.time()
        print('call %s() in %fs' % (f.__name__, (t_end - t_start)))
        return r
    return fn

# @performance
# def factorial(n):
#     return reduce(lambda x, y: x * y, range(1, n + 1))
#
# print('%d! =' % 10, factorial(10))


# 偏函数存在的意义
# 当函数的参数个数太多，需要简化时，使用
# '[functools]partial'可以创建一个新的函数，这个新函数可以固定住原函数的部分参数

