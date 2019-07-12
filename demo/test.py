#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yezhu2'

print('---我爱野猪')
temp = input('请输入年龄:\n')
while True:
    if temp.isdigit():
        guess = int(temp)
        if guess == 8:
            print('答对了')
            break
        elif guess > 8:
            print('大了')
        else:
            print('小了')
        temp = input('请重新输入:\n')
    else:
        print('请必须输入整数')
        temp = input('请重新输入:\n')

print('jieshu')

