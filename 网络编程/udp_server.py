#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   udp_server.py
@Time       :   2019/12/6 21:40
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/6 21:40  helin       1.0         None
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind端口
s.bind(('localhost', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)
    exit(0)

