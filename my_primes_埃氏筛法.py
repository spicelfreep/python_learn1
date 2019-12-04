#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    # 打印1000以内的素数:
    for n in primes():
        if n < 100:
            print(n)
        else:
            break

# 从3开始的奇数序列
def _old_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 然后定义一个筛选函数：质数的
def _not_divisible(n):
    return lambda x : x % n > 0

# 求素数的函数
def primes():
    yield 2
    it = _old_iter()    # 初始序列
    while True:
        n = next(it)    # 返回序列的第一个数
        yield n
        it = filter(_not_divisible, it) # 进去的是列表， 返回的还是列表


if __name__ == '__main__':
    main()