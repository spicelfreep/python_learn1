# -*- coding: UTF-8 -*-
def trim(s):
    if len(s) == 0:
        return '';
    else:
        if len(s) == 1 and s[0] == ' ':
            return ''
        if s[:1] == ' ':
            s = trim(s[1:])
        if s[-1:] == ' ':
            s = trim(s[:-1])
    return s

if trim('hello ') != 'hello':
    print('no')
else:
    print('yes')

if trim('     ') != '':
    print('no')
else:
    print('yes')
