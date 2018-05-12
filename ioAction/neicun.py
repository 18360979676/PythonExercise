#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'

# 内存中读写str--字符串StringIO()

# 内存中读写二进制数据--BytesIO()
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue(), "@")
