#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2019年11月22日14:06:04

def is_odd(n):
    return n % 2 == 0

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['a', 'b', '', ' ', None, 'C'])))
