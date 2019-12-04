#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   fact.py.py
@Time       :   2019/11/27 14:25
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   求阶乘

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 14:25  helin       1.0         None
'''


def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print( fact(5) )
print( fact(10) )
