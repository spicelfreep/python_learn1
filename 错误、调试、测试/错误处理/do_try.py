#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   do_try.py
@Time       :   2019/11/27 12:08
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 12:08  helin       1.0         None
'''

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
    print('except:', e)
finally:
    print('finally...')

print('END')
