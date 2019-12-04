#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   special_getattr.py
@Time       :   2019/11/25 17:09
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/25 17:09  helin       1.0         None
'''


class Student(object):

    def __init__(self):
        self.name = 'Micheal'

    def __getattr__(self, item):
        if item == 'score':
            # 注释
            return 99
        elif item == 'age':
            # 注释
            return lambda : 25
        else:
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

s = Student()
print(s.name)
print(s.score)
print(s.age())
# AttributeError: 'Student' object has no attribute 'grade'
print(s.grade)
