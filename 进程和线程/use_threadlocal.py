#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_threadlocal.py
@Time       :   2019/11/30 22:02
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/30 22:02  helin       1.0         None
'''

import threading

# c创建全局ThreadLocal对象：
local_school = threading.local()


def process_student():
    """
    获取当前线程关联的student
    """
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    """
    绑定ThreadLocal的student：
    """
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice', ), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob', ), name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()

