#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File       :   use_struct.py
@Time       :   2019/12/1 16:01
@Author     :   helin
@Version    :   1.0
@Contact    :   spicalfreep@163.com
@License    :   (C)Copyright 2019-2020
@Desc       :   None

@Modify Time      @Author     @Version    @Desciption
------------      -------     --------    -----------
2019/12/1 16:01  helin       1.0         None
'''

import struct, base64

print('''两个字节：
'BM'表示Windows位图，'BA'表示OS/2位图； 
一个4字节整数：表示位图大小； 
一个4字节整数：保留位，始终为0； 
一个4字节整数：实际图像的偏移量； 
一个4字节整数：Header的字节数； 
一个4字节整数：图像宽度； 
一个4字节整数：图像高度； 
一个2字节整数：始终为1； 
一个2字节整数：颜色数。 ''' )
bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

print(struct.unpack('<ccIIIIIIHH', bmp_header))


def bmp_info(data):
    """
    检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
    """
    bs = struct.unpack('<ccIIIIIIHH', data[:30])
    if bs[:2] == (b'B', b'M'):
        return {
           'width': bs[6],
           'height': bs[7],
            'color': bs[9]
        }

    else:
        return None


bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

bi = bmp_info(bmp_data)
print('bi =', bi)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
