#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   special_str.py
@Time       :   2019/11/25 16:40
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/25 16:40  helin       1.0         None
'''


class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

print(Student('lili'))
