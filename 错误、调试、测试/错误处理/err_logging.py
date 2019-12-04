#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   err_logging.py
@Time       :   2019/11/27 12:14
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 12:14  helin       1.0         None
'''

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar(0)
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    main()
    print('END, 程序没有结束运行')

