#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   hanoi.py.py
@Time       :   2019/11/27 14:32
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   汉诺塔

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 14:32  helin       1.0         None
'''


def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)
# 调用
hanoi(5, 'A', 'B', 'C')
