#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   mydict.py
@Time       :   2019/11/27 13:33
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/27 13:33  helin       1.0         None
'''


class Dict(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError as e:
            raise AttributeError(r"'Dict' object has no attribute %s" % item)

    def __setattr__(self, key, value):
        self[key] = value
