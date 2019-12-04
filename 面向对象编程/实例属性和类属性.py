#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   实例属性和类属性.py
@Time       :   2019/11/23 15:25
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：


@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 15:25  helin       1.0         为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
'''

class Student():
    """
    Student类用于
    """
    count = 0
    def __init__(self, name):
        """
        方法用于
        """
        self.name = name
        Student.count = Student.count + 1


# 测试
if Student.count != 0:
    # 注释
    print('Student.count=', Student.count)
    print('测试失败')
else:
    # 注释
    bart = Student('bart')
    if Student.count != 1:
        # 注释
        print('Student.count=', Student.count)
        print('测试失败')
    else:
        # 注释
        lisa = Student('bart')
        if Student.count != 2:
            # 注释
            print('Student.count=', Student.count)
            print('测试失败')
        else:
            print('Student.count=', Student.count)
            print('测试成功')
