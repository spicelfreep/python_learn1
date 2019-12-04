#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   special_iter.py
@Time       :   2019/11/25 16:52
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/25 16:52  helin       1.0         None
'''

class Fib(object):

    def __init__(self):
        # 初始化两个计数器a，b
        self.a = 0
        self.b = 1

    def __iter__(self):
        # 实例本身就是迭代对象，故返回自己
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:
            raise StopIteration
        return self.a  # 返回下一个值

for i in Fib():
    print(i)
