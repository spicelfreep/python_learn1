#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   do_subprocess.py
@Time       :   2019/11/29 7:50
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/29 7:50  helin       1.0         None
'''

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
