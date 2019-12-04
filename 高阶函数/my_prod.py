#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

def prod(L):
    return reduce(fn, L)

def fn (x, y):
    return x * y


L1 = [ x for x in range(10) ][1:]

print(prod(L1))
