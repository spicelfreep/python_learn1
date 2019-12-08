#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   send_mail.py
@Time       :   2019/12/9 6:25
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/9 6:25  helin       1.0         None
'''

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib


def _format_addr(s):
    """
    方法用于
    """
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# _format_addr('abc')

from_addr = 'spicalfreep@163.com'
# password = 'heghukjopll6'
# password = 'kingrinf@oll0'
password = 'm31pfmbbnn'
to_addr = '1543939425@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

