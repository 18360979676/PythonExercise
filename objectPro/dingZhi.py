#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__


# 斐波那契数列
class Fib(object):
    def __init__(self, n):
        self.a, self.b, self.n = 0, 1, n

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration()
        return self.a


if __name__ == '__main__':

    # print(Student('lyl'))
    for n in Fib(98):
        print(n)
