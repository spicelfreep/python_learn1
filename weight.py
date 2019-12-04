# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight/(height * height)
if bmi <=18.5:
    print('11')
elif 18.5 <= bmi <= 25:
    print('22')
elif 25 <= bmi <= 28:
    print('33')
elif 28 <= bmi <= 32:
    print('44')
elif 32 <= bmi:
    print('55')
