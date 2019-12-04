#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2019年11月22日14:39:34

def main():
    # 测试:
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
    pass

    counterC = createCounter2()
    if [counterC(), counterC(), counterC(), counterC()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
    pass

def createCounter2():
    def plus():
        j = 0
        while True:
            j = j + 1
            yield j
    x = plus()
    def counter():
        return next(x)
    return counter

def createCounter():
    j = 0
    def counter():
        nonlocal j
        j = j + 1
        return j
    return counter

if __name__ == '__main__':
    main()
