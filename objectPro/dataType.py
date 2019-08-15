#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'


class Student(object):

    """使用装饰器来实现"""
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2019 - self._birth


if __name__ == '__main__':
    s = Student()
    s.score = 60
    s.birth = 1993

    print('成绩是:{0},年龄是:{1}'.format(s.score, s.age))
