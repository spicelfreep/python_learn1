#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   1.py
@Time       :   2019/11/30 22:40
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/30 22:40  helin       1.0         None
'''

a = '''
在Thread和Process中，应当优选Process，因为Process更稳定，而且，
Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的
多个CPU上。

Python的multiprocessing模块不但支持多进程，其中managers子模块
还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任
务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，
不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
'''
print(a)
