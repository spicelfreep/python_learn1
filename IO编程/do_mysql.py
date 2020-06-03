#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector
import datetime
import json

config = {
    'user': 'hty',
    'password': 'admin123',
    'host': '10.180.154.192',
    'database': 'dict_server',
    'use_pure': True,
}
# change root password to yours:
conn = mysql.connector.connect(user='hty', password='admin123', database='dict_server', use_pure=True, charset='utf8', host='10.180.154.192')

cursor = conn.cursor()
# cursor.execute('drop table if exists `dicts`')
# 创建user表:
# create_sql = '''\
#  create table if not exists dicts (
#  id int(10) unsigned auto_increment primary key,
#  name varchar(32),
#  created_at timestamp
#  ) charset=utf8
#  '''
Time = datetime.datetime.now() #系统当前时刻
# print(Time)
# exit(1)
fpath = r'D:\project\code\dict\KaoYan\1521164669833_KaoYan_1\KaoYan_1.json'
f = open(fpath, 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if line:
        print(0)
        print(line)
        s = json.loads(line)
        print(s["wordRank"])
        print(s["headWord"])
        print(s["content"])
        print(s["bookId"])
        cursor.execute('INSERT INTO dicts (id, headWord, content, bookId) values (%s, %s, %s, %s)', (0, s['headWord'], json.dumps(s['content']), s['bookId']))
        conn.commit()
    else:
        # pass
        break
f.close()

fpath = r'D:\project\code\dict\KaoYan\1521164654696_KaoYan_2\KaoYan_2.json'

# with open(fpath, 'r', encoding='UTF-8') as f:
#     s = f.read()
#     print(s)
    # s = json.loads(s)

    # print(s["wordRank"])
f = open(fpath, 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if line:
        print(0)
        print(line)
        s = json.loads(line)
        print(s["wordRank"])
        print(s["headWord"])
        print(s["content"])
        print(s["bookId"])
        cursor.execute('INSERT INTO dicts (id, headWord, content, bookId) values (%s, %s, %s, %s)', (0, s['headWord'], json.dumps(s['content']), s['bookId']))
        conn.commit()
    else:
        # pass
        break
f.close()

fpath = r'D:\project\code\dict\KaoYan\1521164658897_KaoYan_3\KaoYan_3.json'
f = open(fpath, 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if line:
        print(0)
        print(line)
        s = json.loads(line)
        print(s["wordRank"])
        print(s["headWord"])
        print(s["content"])
        print(s["bookId"])
        cursor.execute('INSERT INTO dicts (id, headWord, content, bookId) values (%s, %s, %s, %s)', (0, s['headWord'], json.dumps(s['content']), s['bookId']))
        conn.commit()
    else:
        # pass
        break
f.close()

# cursor.execute(create_sql)
# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('INSERT INTO dicts (id, name, created_at) values (%s, %s, %s)', (0, 'Michael', Time))
# cursor.execute('INSERT INTO dicts (id, name, created_at) values (%s, %s, %s)', (0, 'Jone', Time))
# cursor.execute('INSERT INTO dicts (id, name, created_at) values (%s, %s, %s)', (0, 'Max', Time))
# cursor.execute('INSERT INTO dicts (id, name, created_at) values (%s, %s, %s)', (0, '李丹', Time))
# print('rowcount =', cursor.rowcount)
# 提交事务:
# conn.commit()
cursor.close()

# 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from dicts order by id desc limit 1 ')
# values = cursor.fetchall()
# print(values)
# 关闭Cursor和Connection:
# cursor.close()
# conn.close()
