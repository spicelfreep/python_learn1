#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   匿名函数.py
@Time       :   2019/11/22 16:22
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/22 16:22  helin       1.0         None
'''

L1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L1)

# lambda 表达式
L = list(filter(lambda x: x % 2 == 0, range(1, 21)))
print(L)
