#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_enum_gender.py
@Time       :   2019/11/25 17:39
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   把Student的gender属性改造为枚举类型，可以避免使用字符串：

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/25 17:39  helin       1.0         None
'''

from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)

if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
