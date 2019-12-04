#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   make_base64.py
@Time       :   2019/12/1 15:34
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/1 15:34  helin       1.0         None
'''

import base64

def safe_base64_decode(s):
    n = len(s) % 4
    if n != 0:
        for i in range(4-n):
            s = s + b'='
    return base64.b64decode(s)

# safe_base64_decode(b'YWJjZA==')
# safe_base64_decode(b'YWJjZA')

# test:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
