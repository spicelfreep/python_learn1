#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_enum.py
@Time       :   2019/11/25 17:25
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/25 17:25  helin       1.0         可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
'''

from enum import Enum, unique

@unique
class Weekday(Enum):

    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon

print('day1= ', day1)
print('Weekday.Tue', Weekday.Tue)
print('Weekday[\'Tue\']', Weekday.Tue.value)

print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


