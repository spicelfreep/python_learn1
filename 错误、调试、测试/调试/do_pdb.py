#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   do_pdb.py
@Time       :   2019/11/27 12:58
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 12:58  helin       1.0         None
'''

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
