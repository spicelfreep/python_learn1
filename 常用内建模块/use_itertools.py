#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_itertools.py
@Time       :   2019/12/1 17:23
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/1 17:23  helin       1.0         None
'''

import itertools

natuals = itertools.count(1)
sr = ''
for n in natuals:
    sr = sr + '|' + str(n)
    if n >= 100:
        break
sr = sr + '|'
print(sr)

cs = itertools.cycle('ABC')
t = 10
csr = ''
for c in cs:
    csr = csr + c
    # print(c)
    t = t - 1
    if t == 0:
        break
print(csr)

ns = itertools.repeat('R', 19)
nsr = ''
for n in ns:
    nsr = nsr + n
print(nsr)

cr = ''
for c in itertools.chain('ABC', 'XYZ'):
    cr = cr + c
print(cr)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# 计算圆周率可以根据公式：
print('''
计算圆周率可以根据公式：''')

def pi(N):
    """
    计算pi的值
    """
    # step 1: 创建一个奇数序列： 1,3,5...
    number = itertools.count(start=1, step=2)
    # print('number', number)

    # step 2: 取该序列的前N项： 1,3,5,7,9 ... 2*N-1
    result = itertools.takewhile(lambda x: x <= 2*N-1, number)

    # step 3: 添加正负符号并用4除：4/1, -4/3, 4/5, -4/7, 4/9, ...
    n = map(lambda x: (-1)**((x//2) % 2)*4/x, result)

    # step 4: 求和：
    return sum(n)

l = map(lambda x: (-1)**((x//2) % 2)*4/x, [x for x in range(10) if x % 2 == 1])
# print(list(l))
# print(sum(l))
# print(sum(list(l)))
# print(map(lambda x: (-1), [x for x in range(10) if x % 2 == 1]))

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

