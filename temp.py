#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print(100 + 200 + 300)


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









