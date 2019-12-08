#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   send_file_mail.py
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
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
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
password = 'm31pfmbbnn'
to_addr = '1543939425@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()
msg.attach(MIMEText('Send with file...', 'plain', 'utf-8'))

with open('./test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型：
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用base64编码：
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)
server.starttls() # 加密SMTP
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

