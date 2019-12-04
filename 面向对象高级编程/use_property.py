#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_property.py
@Time       :   2019/11/24 0:17
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/24 0:17  helin       1.0         None
'''

class Student(object):
    """
    Student类用于
    """
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            # 注释
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            # 注释
            raise ValueError('score must between 1-100')
        self._score = value

s = Student()
s.score = 94
print('s.score=', s.score)
# ValueError
try:
    s.score = 9999
    print('s.score=', s.score)
except AttributeError as e:
    print('AttributeError:', e)

try:
    s.score = '999'
    print('s.score=', s.score)
except AttributeError as e:
    print('AttributeError:', e)
