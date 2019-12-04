#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_urllib_json.py
@Time       :   2019/12/1 20:09
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/1 20:09  helin       1.0         None
'''

print('''
利用urllib读取JSON，然后将JSON解析为Python对象：''')

from urllib import request
import json


def fetch_data(url):
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        return json.loads(f.read().decode('utf-8'))

# 测试
URL = 'http://arw.me/api/user/test'
data = fetch_data(URL)
print(data)
assert data['name'] == 'admin'
print('ok')
