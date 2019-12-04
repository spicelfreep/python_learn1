# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   do_sorted.py.py
@Time       :   2019/11/22 13:11
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   高阶函数-sorted

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 13:11  helin       1.0         None
'''


def main():
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L1 = sorted(L, key=by_name)
    L2 = sorted(L, key=by_score)
    print(L1)
    print(L2)

def by_name(T):
    # sorted(L, key=)
    # print(T[0])
    return T[0]

def by_score(T):
    # print(T[1])
    return T[1]

if __name__ == '__main__':
    main()
