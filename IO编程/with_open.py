#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   with_open.py
@Time       :   2019/11/27 18:06
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 18:06  helin       1.0         None
'''
from datetime import datetime

with open('test.txt', 'w') as f:
    print('open for write...')
    f.write('今天是1 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'a') as f:
    print('open for write...')
    f.write('今天是2 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    test = f.read()
    print('open for reading...')
    print(test)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for reading...')
    print(s)

