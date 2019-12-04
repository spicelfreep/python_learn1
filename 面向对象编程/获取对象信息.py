#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   获取对象信息.py
@Time       :   2019/11/23 14:59
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 14:59  helin       1.0         None
'''

'''
get_type
'''
print('type(123)', type(123))
print('type(\'123\')', type('123'))
print('type(None)', type(None))
print('type(abc)', type(abs))

# import types

print('type(\'abc\') == str?', type('abc') == str)

'''
attrs
'''
class MyObject():
    """
    MyObject类用于
    """

    def __init__(self):
        """
        方法用于
        """
        self.x = 9
    def power(self):
        """
        方法用于
        """
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\')', hasattr(obj, 'x'))
print('hasattr(obj, \'y\')', hasattr(obj, 'y'))

setattr(obj, 'y', 19)

print('hasattr(obj, \'y\')', hasattr(obj, 'y'))
print('getattr(obj, \'y\')', getattr(obj, 'y'))
print('obj.y=', obj.y)

print('getattr(obj, \'z\')', getattr(obj, 'z', 780))

f = getattr(obj, 'power')
print(f)
print(f())

print('''请注意，在Python这类动态语言中，
根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，
它也可能是网络流，也可能是内存中的一个字节流，
但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。''')
