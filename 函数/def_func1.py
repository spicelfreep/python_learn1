#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   def_func1.py.py
@Time       :   2019/11/27 13:57
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   计算三个系数组成的方程的根

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 13:57  helin       1.0         计算三个系数组成的方程的根
'''

import math

def quadratic(a, b, c):
    #print(math.sqrt(b*b-4*a*c))
    #print((-b + math.sqrt(b*b-4*a*c)))
    #print((-b - math.sqrt(b*b-4*a*c)))
    x = (-b + math.sqrt(b*b-4*a*c))/(2*a)
    y = (-b - math.sqrt(b*b-4*a*c))/(2*a)
    return (x, y)

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
else:
    print('测试成功')

if quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
