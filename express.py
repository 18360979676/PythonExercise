#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'

import re
# print(re.match(r'\d{3}\-\d{3,8}', '400-77777777'))
# print(re.split(r'[\s\d]+', 'a v  3'))
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')


def result():
    return m


# 编译正则表达式：
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# print(re_telephone.match('010-123456').groups())


# 匹配所有电子邮箱
def is_valid_email(addr):
    temp_value = re.match(r'^([0-9a-zA-Z_]{0,19})@([0-9a-zA-Z]{1,13}\.[com,net,cn]{1,3})$', addr)
    if temp_value:
        print('email is valid', temp_value.groups()[0])
    else:
        print('emial is invalid')


is_valid_email(input('请输入要验证的电子邮箱地址'))
