#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print(100 + 200 + 300)
# 索引

# print('The quick brown fox', 'jumps over', 'the lazy dog')


# name = input()    捕捉用户控制台的输入
# print('hello,', name)


# name = input()
# if name == 'lyl123':
#     print('正确')
# else:
#     print('错误')

# n = 123
# f = 456.789
# s1 = 'hello, world'
# s2 = 'hello, \'Adam\''
# s3 = r'Hello, \'Bart\''
# s4 = r'''Hello,\n
#     Lisa!'''
# print(s3)

# #字符编码成字节
# encode_str = 'ABC'.encode('ascii')
# encode_str = encode_str.decode('ascii')
# print(encode_str)


#计算字符串包含的字符数目

# print('ABC-包含的字符数目', len(b'ABC'))
# print('中文-包含的字符数目', len('中文'))

#格式化
# print('pi * pi =', '%.2f' % 3.1415926, '大爷的')

#format()格式化函数
# print('Hello, {0}, 成绩提升了 {1:.3f}%'.format('小明', 17.125))


#list集合=>可变的有序表


#tuple有序列表=>经过初始化就不能继续修改了


#条件判断
# age = input('输入法定年龄:')
# if int(age) >= 18:
#     print('成年了')
# else:
#     print('未成年')


#for-in循环语句
# sum = 0
# for i in range(101):
#     sum = sum + i
# print(sum)

#while循环语句
# sum = 0
# n, index = 99, 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print('n = {0}的累计和为'.format(index), sum)


#exercise=》展示数组所有的元素
# L = ['lyl', 'abc', 'def']
# for index in L:
#     print('hello ', index)


#set和dict类似，也是一组key的集合，但不存储value
# s = set([1, 2, 3])
# print(s)


#定义函数
#在命令行交互模式运行的方式 from 函数所在的文件名fileName import 函数名称funName
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# print(my_abs(-9))

#定义空函数,起到占位符的作用
def nop():
    pass

#计算某个数字的n次方
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
# print('{0}的{1}次方等于'.format(5, 2), power(5, 2))


#函定函数的默认参数尽量使用不变对象
def add_end(L = None):
    if L is None:
        L = []
    L.append('end')
    return L


#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它
def f3(**args):
    sum, beichushu, chushu = 0, 0, 0
    for i in args:
        if i == 'a':
            beichushu = args[i]
        elif i == 'b':
            chushu = args[i]
    sum = beichushu / chushu
    return sum

# print('关键字参数传参方式--%d/%d ='%(5, 2), f3(a = 5, b = 2))


#定义递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# inputString = input('请输入要进行递归运算的数字:')
# inputInt = int(inputString)
# print('%d的递归运算是:' % inputInt, fact(inputInt))


#高级特性--切片操作取出字符串两端的空格
def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])


#迭代--字典的key、value、键值对
# d = {'a': 1, 'b': 2}
# for key in d:
#     print(key)
# for value in d.values():
#     print(value)
# for k, v in d.items():
#     print(k, ':', v)


#判断一个对象是否可以迭代
# from collections import Iterable
# print('判断%s是否可以迭代' % 'abc', isinstance('abc', Iterable))

#迭代索引和元素本身
# for i, value in enumerate(['a', 'b', 'c']):
#     print('d[{0}] = {1}'.format(i, value))


#查找list集合的最大值和最小值
# list = [1, 6, 4, 2]
# max, min = list[0], list[0]
# print(max, min)
# for index in list:
#     if index > max:
#         max = index
#     elif index < min:
#         min = index
# print('集合{0}的最大值为{1}, 最小值为 {2}'.format(list, max, min))


#列表生成式--列出当前目录的所有文件和目录名称
# import os
# print([d for d in os.listdir('.')])

#同时使用两个变量生成list
# print([k + '=' + v for k, v in {'one': '1', 'two': '2', 'three': '3'}.items()])

#把list列表中的字符串全部修改为小写字母, 移除数字
# listAll = [s.lower() for s in ["DFDF", 4545, 'SDSSD'] if isinstance(s,(str))]
# print(listAll)

#生成器生成斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

#迭代器--判断对象是否可以迭代
# from collections import Iterable
# print(isinstance([], Iterable))

#for循环本质上就是通过不断调用next()函数实现
# for x in [1, 2, 3, 4, 5]:
#     pass
#完全等效于下面的方程式
# it =  iter([1, 2, 3, 4, 5])
# while True:
#     try:
#         #获得下一个数值
#         x = next(it)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break



