#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_metaclass.py
@Time       :   2019/11/27 8:55
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 8:55  helin       1.0         None
'''

# metaclass 是创建类，所以必须从‘type’类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 指示使用ListMetaclass来定制类
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)
