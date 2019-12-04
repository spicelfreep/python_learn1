# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   返回函数.py.py
@Time       :   2019/11/23 13:10
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 13:10  helin       1.0         None
'''


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())

# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

# fix:
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    print('fs:', fs)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

F = count()

for n in F:
    print(n())

print(F[0]())
print(F[1]())
print(F[2]())
