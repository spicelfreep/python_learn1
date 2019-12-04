#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_contextlib.py
@Time       :   2019/12/1 18:29
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/1 18:29  helin       1.0         None
'''

print('''
可以把自己写的资源对象用于with语句： ''')

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        """
        方法用
        """
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()

print(''' 
@contextmanager
编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下： ''')

from contextlib import contextmanager


class Query2(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query1 info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')
with create_query('Bob') as q:
    q.query()

print('''
很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如： ''')
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


with tag("h1"):
    print("Hello")
    print("World")

print(''' 因此，@contextmanager让我们通过编写generator来简化上下文管理。 ''')

print('''
@closing
如果一个对象没有实现上下文，我们就不能把它用于with语句。
这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()： ''')

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)

print('''
closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单： ''')
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

print('''它的作用就是把任意对象变为上下文对象，并支持with语句。 ''')
print('''@contextlib还有一些其他decorator，便于我们编写更简洁的代码。 ''')
