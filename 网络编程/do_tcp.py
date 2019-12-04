#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   do_tcp.py
@Time       :   2019/12/5 7:27
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/5 7:27  helin       1.0         None
'''

import socket

# 创建一个socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接：
s.connect( ('www.sina.com.cn', 80) )

# 发送数据：
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据：
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

# 关闭连接
s.close()
print(data)
print('End OK.')
