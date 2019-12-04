#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   my_use_property.py
@Time       :   2019/11/24 0:34
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/24 0:34  helin       1.0         None
'''

class Screen(object):

    def __init__(self):
        self._resolution = 786432

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('value must be an integer')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('value must be an integer')
        self._height = value

    @property
    def resolution(self):
        return self._resolution

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('s.width =', s.width)
print('s.height =', s.height)
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
    s.resolution = 343
else:
    print('测试失败!')



