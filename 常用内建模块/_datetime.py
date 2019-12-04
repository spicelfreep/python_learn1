#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   datetime.py
@Time       :   2019/12/1 11:18
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/1 11:18  helin       1.0         None
'''

from datetime import datetime, timedelta, timezone

now = datetime.now()    # 获取当前datetime
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2018, 4, 19, 19, 23, 20)
print(dt)

# datetime转换为timestamp
dtt = dt.timestamp()
print(dtt)

#timestamp转换为datetime
dt2 = datetime.fromtimestamp(dtt)
print(dt2)

# timestamp也可以直接被转换到UTC标准时区的时间：
dt3 = datetime.utcfromtimestamp(dtt)
print(dt3)

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# cday = datetime.strptime('2015年6月1日 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a %b %d %H %M'))

# datetime加减
print('datetime加减')
'''
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
'''
# now = datetime.now()

print(now)
print(now + timedelta(hours=10))
print(now + timedelta(days=2, hours=10))
print(now - timedelta(hours=10))
print(now - timedelta(days=2, hours=10))

# 本地时间转换为UTC时间
print( '''
本地时间转换为UTC时间
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。 ''')

tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)

dt =  now.replace(tzinfo=tz_utc_8)
print(dt)

print('''
时区转换 
我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
''')
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))

print(tokyo_dt2)
print('注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。 ')

print('''
小结
datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。''')

print('''
练习
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：''')

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
     dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
     m = re.match(r'^UTC([+\-]\d{1,2}):(\d{1,2})$', tz_str)
     if not m:
         return None
     h = int(m.group(1))
     m = int(m.group(2))
     s = h * 60 * 60 + m * 60
     tz = timezone(timedelta(0, s))
     dt_utc = dt.replace(tzinfo=tz)
     return dt_utc.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('ok')

