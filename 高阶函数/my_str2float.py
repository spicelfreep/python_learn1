#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2019年11月22日15:48:11
# 高阶函数--reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}

def char2num(s):
    return DIGITS[s]

def str2float(s):
    # nums = map(lambda ch: DIGITS[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, list(map(char2num, s)), 0.0)

print(list(map(char2num, '123.456')))

print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')