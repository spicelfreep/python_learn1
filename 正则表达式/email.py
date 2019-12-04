#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   email.py
@Time       :   2019/12/1 10:16
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/1 10:16  helin       1.0         None
'''

import re


def is_valid_email(addr):
    """
    方法用于验证合法email地址
    """
    # if re.match('^[0-9a-zA-Z\_]+\.[0-9a-zA-Z\_]+|[0-9a-zA-Z\_]+@\w+.com$', addr):
    if re.match(r'^[\w\_]+\.[\w\_]+|[0-9a-zA-Z\_]+@\w+\.\w+$', addr):
            return True
    else:
        return False

if is_valid_email('someone@gmail.com'):
    print('someone@gmail.com is ok')
else:
    print('someone@gmail.com is not ok')

if is_valid_email('bill.gates@microsoft.com'):
    print('bill.gates@microsoft.com is ok')
else:
    print('bill.gates@microsoft.com is not ok')


def name_of_email(addr):
    """
    方法用于:提取出带名字的Email地址
    """
    # m = re.match(r'^<?([\w\s.]+)>?\s?([\w\_]+\.[\w\_]+|[0-9a-zA-Z\_]+)@\w+\.\w+$', addr)
    m = re.match(r'^<?([\w\s.]+)>?\s?([\w\s]*)@\w+\.\w+$', addr)
    if m:
        if m.group(1):
            print(r'group1', m.group(1))
        else:
            print(r'group2', m.group(2))

    else:
        print(r'group1 ...')


name_of_email('someone@gmail.com')
name_of_email('bill.gates@microsoft.com')
name_of_email('<Tom Paris> tom@voyager.org')
