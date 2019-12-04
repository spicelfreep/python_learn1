# -*- coding: utf-8 -*-

def product(*arg):
    if len(arg) == 0 :
        return 0
    # if len(arg) < 2 :
    #     print('参数太少')
    sum = 1;
    for x in arg:
        sum = sum * x
    return sum

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        if product() != 0:
            print('测试失败!')
    except TypeError:
        print('测试失败!')

print('END')
