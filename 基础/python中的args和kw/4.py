#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   4.py
@Time       :   2019/11/27 15:43
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 15:43  helin       1.0         None
'''

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1)
print(f2)
print(f3)

print(f1())
print(f2())
print(f3())
