#!/usr/bin/env python
# -*- coding: utf-8 -*-

print u'中文字符串测试-正常'

# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('%s' % ('hhhhhh'))
print('%05d' % (18))
print('%.2f' % (3.1415926))

print('Age: %s. Gender: %s' % (25, True))
print(u'Hi, %s' % u'Michael')
print(u'中文'.encode('gb2312'))