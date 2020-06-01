#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def do_fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    # return 'done'
    print('done')

g = do_fib(10)
for n in g:
    print('g1:', n)

fib(10)

g = do_fib(10)
while True:
    try:
        x = next(g)
        print('g2:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break