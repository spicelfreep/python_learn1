#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   do_logging.py
@Time       :   2019/11/27 12:56
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 12:56  helin       1.0         None
'''

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
