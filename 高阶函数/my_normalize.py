#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# a = 'a'
# print('a' - 26)

def cap(str):
    str1 = ''
    for k, v in enumerate(str):
        if k == 0:
            str1 = str1 + v.upper()
        else:
            str1 = str1 + v.lower()
    return str1

def normalize(name):
    # return name.capitalize()
    return cap(name)

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
