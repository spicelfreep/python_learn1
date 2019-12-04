#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   偏函数.py.py
@Time       :   2019/11/23 12:56
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/23 12:56  helin       1.0         None
'''

import functools

def main():
    int2 = functools.partial(int, base=2)
    print('1000000=', int2('1000000'))
    print('1010101=', int2('1010101'))

    max2 = functools.partial(max, 10)
    print('max2', max2(4,5,6))

    return True

if __name__ == '__main__':
    main()

