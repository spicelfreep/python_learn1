#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   task_master.py
@Time       :   2019/11/30 23:55
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/11/30 23:55  helin       1.0         None
'''

import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue =  queue.Queue()  # 发送任务的队列:
result_queue = queue.Queue() # 接收结果的队列:
class QueueManager(BaseManager):  # 从BaseManager继承的QueueManager:
    pass
# windows下运行
def return_task_queue():
    global task_queue
    return task_queue  # 返回发送任务队列
def return_result_queue ():
    global result_queue
    return result_queue # 返回接收结果队列

def test():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象,它们用来进行进程间通信，交换对象
    #QueueManager.register('get_task_queue', callable=lambda: task_queue)
    #QueueManager.register('get_result_queue', callable=lambda: result_queue)
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000, 设置验证码'abc':
    #manager = QueueManager(address=('', 5000), authkey=b'abc')
    # windows需要写ip地址
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()  # 启动Queue:
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(10):   # 放几个任务进去:
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        # 这里加了异常捕获
        try:
            r = result.get(timeout=5)
            print('Result: %s' % r)
        except queue.Empty:
             print('result queue is empty.')
    # 关闭:
    manager.shutdown()
    print('master exit.')
if __name__=='__main__':
    freeze_support()
    print('start!')
    test()


