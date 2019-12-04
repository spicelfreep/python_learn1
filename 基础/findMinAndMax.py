# -*- coding: utf-8 -*-
def findMinAndMax(items):
    if len(items)==0:
        return(None,None)
    min=max=items[0]
    for item in items:
        if item > max:
            max = item
        if item < min:
            min = item
    return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('fail!')
elif findMinAndMax([7]) != (7, 7):
    print('fail!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('fail!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('fail!')
else:
    print('ok!')
