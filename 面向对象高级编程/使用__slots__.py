#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   使用__slots__.py
@Time       :   2019/11/23 15:36
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 15:36  helin       1.0         None
'''

class Student():
    """
    S类用于
    """
    __slots__ = ('name', 'age')


class GraduateStudent(Student):
    pass

s = Student()

s.name = 'zhansan'
s.age = 67

try:
    s.score = 100
except AttributeError as e:
    print('AttributeError:', e)


g = GraduateStudent()
g.score = 99

print('g.score=', g.score)
