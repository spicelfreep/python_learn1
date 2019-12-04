#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   路灯安置.py
@Time       :   2019/11/25 14:09
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/25 14:09  helin       1.0         None
'''

n = input()
N = []
for i in range(int(n)):
    count = input()
    line = input()
    c = 0
    tmp = ''
    res = 0
    # L = []
    for k, i in enumerate(line):
        if i == '.':
            c += 1
            tmp += '.'
        if i == 'X':
            if c > 0 and c < 3:
                c += 1
                tmp += 'X'
        if k+1 == int(count):
            # 注释
            if c > 0:
                if tmp == 'X' or tmp == 'XX' or tmp == 'XXX':
                    pass
                else:
                    # L.append(tmp)
                    res += 1
                    c = 0
                    tmp = ''
        else:
            # 注释
            if c == 3:
                # L.append(tmp)
                res += 1
                c = 0
                tmp = ''
    # print(len(L))
    N.append(res)

# print(N)
for i in N:
    # 注释
    print(i)
