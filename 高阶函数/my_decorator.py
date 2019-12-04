#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   my_decorator.py.py
@Time       :   2019/11/23 12:56
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 12:56  helin       1.0         None
'''

import time, functools

def metric(func):
    print('%s executed in %s ms' % (func.__name__, 10.24))
    @functools.wraps(func)
    def wapper(*args, **kw):
        print('call %s():' % (func.__name__))
        return func(*args, **kw)
    return wapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')

