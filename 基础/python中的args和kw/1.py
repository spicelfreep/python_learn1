#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   python中的args和kw.py
@Time       :   2019/11/27 14:49
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 14:49  helin       1.0         None
'''

def foo(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)
foo(1,2,3,4,y=1,a=2,b=3,c=4)#将1传给了x，将2,3,4以元组方式传给了args，y=1,a=2,b=3,c=4以字典的方式给了kwargs

# 1
# (1, 2, 3)
# {'y': 1, 'a': 2, 'b': 3 'c': 4}
