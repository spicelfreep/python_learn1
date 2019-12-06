#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   test.py
@Time       :   2019/11/28 7:23
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/28 7:23  helin       1.0         None
'''

import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
s2 = json.dumps(obj, ensure_ascii=False)
print(s)
print(s2)