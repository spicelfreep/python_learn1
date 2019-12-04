#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   文件读写.py
@Time       :   2019/11/27 16:26
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 16:26  helin       1.0         None
'''

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

