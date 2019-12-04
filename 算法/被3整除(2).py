#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   被3整除(2).py
@Time       :   2019/11/25 13:33
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/25 13:33  helin       1.0         None
'''


# line = input('请输入您的内容：\n')
line = input()
# print(line)
l, r = line.strip().split()   # 7  1
l = int(l)
r = int(r)

res = 0
for i in range(l, r+1):
    if ((i*(i+1))/2) % 3 == 0 :  #  算法 复杂度过大
        # 注释
        res += 1

print(res)

'''运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为70.00%'''
