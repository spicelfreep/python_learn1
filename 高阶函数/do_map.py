#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   do_map.py.py
@Time       :   2019年11月22日15:51
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 12:57  helin       1.0         None
'''


def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))