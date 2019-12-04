#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   do_assert.py
@Time       :   2019/11/27 12:53
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 12:53  helin       1.0         None
'''

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()
