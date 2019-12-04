#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   err_raise.py
@Time       :   2019/11/27 12:20
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 12:20  helin       1.0         None
'''


class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        # 注释
        raise FooError('Invalid value:%s' % s)
    return 10/n

foo('0')
