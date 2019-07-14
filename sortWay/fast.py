#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/7/13 21:30
#@Author: yezhu
#@File  : fast.py

def quick_sort(arr):
    """快速排序"""
    if len(arr) < 2:
        return arr
    mid = arr[len(arr) // 2]
    left, right = [], []
    arr.remove(mid)
    for item in arr:
        if item >= mid:
            right.append(item)
        else:
            left.append(item)
    return quick_sort(left) + [mid] + quick_sort(right)



if __name__ == '__main__':
    temp_arr = [23, 56, 12, 1, 2, 3, 4, 5, 6]
    for item in quick_sort(temp_arr):
        print(item, end=" ")
