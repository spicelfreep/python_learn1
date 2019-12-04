#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   面向对象编程.py
@Time       :   2019/11/23 13:50
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 13:50  helin       1.0         None
'''

class Student():
    """
    Student类用于
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score


    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
