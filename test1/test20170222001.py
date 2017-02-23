# coding: utf-8
# 调用函数

import math

r1 = 12.34
r2 = 9.08
r3 = 73.1

s1 = 3.14 * r1 * r1
s2 = 3.14 * r2 * r2
s3 = 3.14 * r3 * r3


def area(r):
    return r ** 2 * math.pi
print area(r1)
print area(r2)

print help(abs)

print abs(-7)

print int('889')
print int(889.5)
print float(889.5)
print str(889)
print unicode(100)
print bool(1)
print bool('')

a = abs
print a(-7)

print cmp(1, 2)
print cmp(2, 2)
print cmp(3, 2)
