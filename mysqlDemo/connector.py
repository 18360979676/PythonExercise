#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/7/22 20:29
#@Author: yezhu
#@File  : connector.py

from mysql.connector import Connect

mydb = Connect(
    host="localhost",  # 数据库主机地址
    user="root",   # 数据库用户名
    passwd="123456",    # 数据库密码
    database="runnoob_db"
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

