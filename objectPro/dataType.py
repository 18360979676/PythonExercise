#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'


class Student(object):

    # def get_score(self):
    #     return self._score
    #
    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('score must be integer!')
    #     if value < 0 or value > 100:
    #         raise ValueError('score must between 0 ~ 100!')
    #     self._score = value

    # 使用装饰器来实现
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
        return 2018 - self._birth


if __name__ == '__main__':
    s = Student()
    # s.set_score(60)  # ok!
    # print(s.get_score())
    #
    # s.set_score(9999)

    s.score = 60
    # s.score = 9999
    s.birth = 1993
    print('成绩是：', s.score, '年龄是:', s.age)
