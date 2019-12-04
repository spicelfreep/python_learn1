#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   regex.py
@Time       :   2019/12/1 11:10
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/1 11:10  helin       1.0         None
'''

import re
print('Test: 010-12345')
test = '010-12345'
m = re.match(r'^(\d{3})-(\d{3,8})$', test)
print(m.group(0), m.group(1), m.group(2))
print(m.groups())

t = '19:23:24'
print('Test', t)
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

