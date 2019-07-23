#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/7/22 20:29
#@Author: yezhu
#@File  : connector.py

from mysql.connector import Connect

mydb = Connect(
    host="localhost",  # 数据库主机地址
    user="root",   # 数据库用户名
    passwd="123456"    # 数据库密码
)

mycursor = mydb.cursor()
mycursor.execute("show databases")
for item in mycursor:
    print(item, end=" ")

if __name__ == '__main__':
    pass