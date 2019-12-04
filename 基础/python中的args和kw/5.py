#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   5.py
@Time       :   2019/11/27 15:53
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   fs当前数组中存储的函数指针把for循环i变量的值作为fs内函数指针的参数

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 15:53  helin       1.0         None
'''

def count():
    fs=[]
    for i in range(1, 4):
        def f(i):
            def g():
                return i * i
            return g
        r = f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()

print(f1)
print(f2)
print(f3)

print(f1())
print(f2())
print(f3())
