#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_hashlib.py
@Time       :   2019/12/1 16:27
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/1 16:27  helin       1.0         None
'''

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use md5'.encode('utf-8'))
sha1.update(' in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

def calc_md5(password):
    '''
    计算password的MD5值
    :param password: str
    :return: str
    '''
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

print(calc_md5('123456'))

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

print('len = ', len('878ef96e86145580c38c87f0410ad153'))


def login(user, password):
    """
    方法用于验证用户登录
    """
    flag = False
    for k, v in db.items():
        if user == k and calc_md5(password) == v:
            flag = True
            break
    return flag

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# 根据用户输入的登录名和口令模拟用户登录，计算更安全的MD5：
print('根据用户输入的登录名和口令模拟用户登录，计算更安全的MD5：')
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):

    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.username + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login1(username, password):
    user = db[username]
    return user.password == get_md5(password + username + user.salt)

# 测试:
assert login1('michael', '123456')
assert login1('bob', 'abc999')
assert login1('alice', 'alice2008')
assert not login1('michael', '1234567')
assert not login1('bob', '123456')
assert not login1('alice', 'Alice2008')
print('ok')
