#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   神奇的数被三整除.py
@Time       :   2019/11/24 14:39
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/24 14:39  helin       1.0         None
'''

'''
问题描述：

小Q得到一个神奇的数列: 1, 12, 123,...12345678910,1234567891011...。

并且小Q对于能否被3整除这个性质很感兴趣。

小Q现在希望你能帮他计算一下从数列的第l个到第r个(包含端点)有多少个数可以被3整除。

输入描述：

输入包括两个整数l和r(1 <= l <= r <= 1e9), 表示要求解的区间两端。
输出描述：

输出一个整数, 表示区间内能被3整除的数字个数。
输入例子1：

2 5
输出例子1：

3
例子说明1：

12, 123, 1234, 12345...
其中12, 123, 12345能被3整除。
————————————————
'''
# line = input('请输入您的内容：\n')
line = input()
# print(line)
l, r = line.strip().split()   # 7  1
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

result = ((r - l) / 3) * 2 - count1 + count2
print('%d' % result)
