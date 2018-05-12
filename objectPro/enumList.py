#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'

# 使用枚举类型
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# 枚举类派生出自定义类
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == '__main__':
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    # 访问自定义的枚举类型
    print('\n', Weekday(1))
