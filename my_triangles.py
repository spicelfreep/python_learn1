# -*- coding: utf-8 -*-
import copy

def triangles(max):
    n = 0
    l = []
    while n < max:
        tmp = copy.deepcopy(l)
        for index, value in enumerate(l):
            if index > 0:
                l[index] = tmp[index] + tmp[index-1]
        l.append(1)
        n = n + 1
        print(l)
    return 'done'

def do_triangles(max):
    n = 0
    l = []
    while n < max:
        tmp = copy.deepcopy(l)
        for index, value in enumerate(l):
            if index > 0:
                l[index] = tmp[index] + tmp[index-1]
        l.append(1)
        n = n + 1
        yield l
    return 'done'

def do_triangles2(max):
    n = 0
    l = []
    while n < max:
        tmp = l[:]
        for index, value in enumerate(l):
            if index > 0:
                l[index] = tmp[index] + tmp[index-1]
        l.append(1)
        n = n + 1
        yield l
    return 'done'

triangles(6)
tr1 = do_triangles(7)
tr2 = do_triangles(8)
while True:
    try:
        x = next(tr1)
        print(x)
    except StopIteration as e:
        print('Generator return value tr1:', e.value)
        break

while True:
    try:
        x = next(tr2)
        print(x)
    except StopIteration as e:
        print('Generator return value tr2:', e.value)
        break
