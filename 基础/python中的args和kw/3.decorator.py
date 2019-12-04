#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   3.decorator.py
@Time       :   2019/11/27 14:59
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 14:59  helin       1.0         None
'''

def new_fun(x):
    return x*2

@new_fun
def f(x):
    return x*2

# f1 = new_fun(f)

f(2)
