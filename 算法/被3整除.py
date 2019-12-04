#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   被3整除.py
@Time       :   2019/11/24 1:20
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/24 1:20  helin       1.0         None
'''

while True:
    # line = input('请输入您的内容：\n')
    line = input()
    # print(line)
    l, r = line.strip().split()  # 7 10
    l = int(l)
    r = int(r)

    count1 = 0
    count2 = 0
    result = 0
    while l % 3 != 1:
        if l % 3 == 0:
            l = l - 1
            count1 = count1 + 1
        if l % 3 == 2:
            l = l - 1

    while r % 3 != 1:
        if r % 3 == 0:
            r = r - 1
            count2 = count2 + 1
        if r % 3 == 2:
            count2 = count2 + 1
            r = r - 1

    print(r, l)
    print(r-l, ((r-l)/3) *2, count1, count2)
    result = ((r-l)/3) *2 - count1 + count2
    # 2 - 2 + 6
    print('%d' % result)
