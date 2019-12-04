#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print(str(1000)[:2])
s='123456'
print("s [::-1]", s[::-1])
print("s [:0:-1]", s[:0:-1])
print("s [:1:-1]", s[:1:-1])
print("s [:2:-1]", s[:2:-1])
print("s [:3:-1]", s[:3:-1])
print("s [:4:-1]", s[:4:-1])
print("s [:5:-1]", s[:5:-1])
print("s [:6:-1]", s[:6:-1])
print("s [:-1:-1]", s[:-1:-1])
print("s [:-2:-1]", s[:-2:-1])
print("s [:-3:-1]", s[:-3:-1])
print("s [:-4:-1]", s[:-4:-1])
print("s [:-5:-1]", s[:-5:-1])
print("s [-1:-5:-1]", s[-1:-5:-1])

print("s [0::-1]", s[0::-1])
print("s [1::-1]", s[1::-1])
print("s [2::-1]", s[2::-1])

print("s [-2::-1]", s[-2::-1])

print("s [3::-1]", s[3::-1])
print("s [-3::-1]", s[-3::-1])
print("s [4::-1]", s[4::-1])
print("s [-4::-1]", s[-4::-1])

print("s [-4:2:-1]", s[-4:2:-1])
print("s [-4:-2:-1]", s[-4:-2:-1])

print("s [3::-1]", s[3::-1])

print("s [:2:-1]", s[:2:-1])

print("s [:3:-1]", s[:3:-1])
# exit(0)

# 计算整数位数
def num_count(n):
    icount = 1
    while n >= 10:
        # print(n)
        n = int(n / 10)
        icount = icount + 1
    return icount

# c = num_count(1000)

# print(c)
# exit(0)

def get_left(n):
    c = num_count(n)
    # print('lc:', c)
    if c == 1:
        left = str(n)

    else:
        if c % 2 == 0:
            c2 = int(c/2)
        else:
            c2 = int((c-1)/2)
            # print('lc2:', c2)
        left = str(n)[:c2]
    # print(left)
    return left

def get_right(n):
    c = num_count(n)
    # print('rc:', c)
    if c == 1:
        r = str(n)
    else:
        if c % 2 == 0:
            c2 = int(c/2)
            r = str(n)[:c2-1:-1]
        else:
            c2 = int((c-1)/2)
            r = str(n)[:c2:-1]
    # print(r)
    return r

# print(get_left(1), get_right(1))
#
# print(get_left(2), get_right(2))
#
# print(get_left(3), get_right(3))
# print(get_left(100) == get_right(100))
# exit(0)

def is_palindrome(x):
    return get_left(x) == get_right(x)

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')