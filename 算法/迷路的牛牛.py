#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   迷路的牛牛.py
@Time       :   2019/11/25 15:31
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/25 15:31  helin       1.0         None
'''

# B = 'N'
D = 'NESW'
c = input()
r = input()
# c = 27
# r = 'LRRRLRRRRRRLRRRLLLLLLRLRLRR'
# r = 'LRRRLRRRRRLLLLLLLLLLLRLRLRR'
cl, cr = 0, 0
for key, value in enumerate(r):
    if value == 'L':
        cl += 1
    if value == 'R':
        cr += 1

ml = cr - cl
k = ml % 4
print(D[k:k+1:])
