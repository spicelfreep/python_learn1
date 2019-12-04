#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_urllib0.py
@Time       :   2019/12/1 18:56
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/1 18:56  helin       1.0         None
'''

print('''
urllib提供了一系列用于操作URL的功能。

Get

urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
''')

from urllib import request

with request.urlopen('https://baidu.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:\n', data.decode('utf-8'))




