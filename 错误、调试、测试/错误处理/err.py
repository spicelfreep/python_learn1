#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   err.py
@Time       :   2019/11/27 12:12
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 12:12  helin       1.0         None
'''

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar(0)


if __name__ == '__main__':
    main()
