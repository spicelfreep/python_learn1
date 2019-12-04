# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   装饰器-作用于任何函数.py
@Time       :   2019/11/23 12:46
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 12:47  helin       1.0         None
'''

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wapper(*agrs, **kw):
        print('call %s():' % (fn.__name__))
        return fn(*agrs, **kw)
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
print(f, s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试通过!')

