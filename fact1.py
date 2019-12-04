#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   fact1.py.py
@Time       :   2019/11/27 14:27
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 14:27  helin       1.0         None
'''


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    print('fact_iter(', num - 1 ,', ',num * product,')')
    return fact_iter(num - 1, num * product)

print( fact(5) )
