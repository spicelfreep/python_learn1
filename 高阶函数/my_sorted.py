#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2019年11月22日14:20:46
# 高阶函数-sorted

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
