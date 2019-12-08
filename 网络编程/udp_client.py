#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   udp_client.py
@Time       :   2019/12/6 21:48
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/6 21:48  helin       1.0         None
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))

s.close()
