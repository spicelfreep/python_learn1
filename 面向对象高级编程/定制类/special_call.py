#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   special_call.py
@Time       :   2019/11/25 17:14
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/25 17:14  helin       1.0         None
'''


class Student(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s.' % self.name)

s = Student('Micheal')

s()
Student('lucy')()
