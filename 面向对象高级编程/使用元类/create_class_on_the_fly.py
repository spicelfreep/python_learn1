#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   create_class_on_the_fly.py
@Time       :   2019/11/27 8:50
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   type()

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 8:50  helin       1.0         None
'''

'''
type()函数既可以返回一个对象的类型，又可以创建出新的类型

要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
'''


def fn(self, name='world'):
    print('Hello, %s!' % name)

Hello = type('Hello', (object, ), dict(hello=fn)) # 创建Hello类

h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello):', type(Hello))
print('type(h)', type(h))
