#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   decorator.py
@Time       :   2019/11/23 12:45
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 12:45  helin       1.0         None
'''

import functools, datetime

def log(func):
    @functools.wraps(func)
    def warpper(*args, **kw):
        print('call %s():'% (func.__name__))
        return func(*args, **kw)
    return warpper

@log
def now():
    print('2019年11月22日16:44:21')

now()


def logger(text):
    # print('call %s():' % (__name__))

    def decorator(func):
        @functools.wraps(func)
        def warpper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return warpper
    return decorator

@logger('DEBUG')
def today():
    print('2019年11月22日16:41:14')

print('call %s():' % (today.__name__))
today()
