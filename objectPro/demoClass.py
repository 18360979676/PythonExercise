#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'


class Student(object):

    # 实例初始化
    def __init__(self, name, score):  # selft-创建的实例本身
        self.__name = name
        self.__score = score

    # 打印学生的成绩
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # 批改学生的成绩等第
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    # 内部方法访问私有变量
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 内部方法修改变量
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


if __name__ == '__main__':
    lisa = Student('Lisa', 99)
    bart = Student('Bart', 59)
    print('{0}成绩为 {1}'.format(lisa.get_name(), lisa.get_grade()))
    print('{0}成绩为 {1}'.format(bart.get_name(), bart.get_grade()))


# 下划线开头的实例变量名/比如_name/这样的实例变量外部是可以访问的/但是/按照约定俗成的规定
# 当你看到这样的变量时/意思就是虽然我可以被访问/但是/请把我视为私有变量/不要随意访问


# 继承和多态
class Animal(object):

    # 基类公有的方法
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


# 对象的内置方法
# dir(obj)---获得一个对象的所有属性和方法list[]格式
# getattr(obj,'')、setattr(obj,'',vlaue)以及hasattr()用来直接操作一个对象的状态
# 可以传入一个default参数，如果属性不存在，就返回默认值
# getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
