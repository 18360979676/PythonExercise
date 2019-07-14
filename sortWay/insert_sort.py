#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/7/14 13:51
#@Author: yezhu
#@File  : insert_sort.py

import unittest

def insert_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr

if __name__ == '__main__':
    arr = [23, 2, 3, 4, 56, 23, 23]
    for item in insert_sort(arr):
        print(item, end=" ")
