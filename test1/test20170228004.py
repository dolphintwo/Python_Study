# coding: utf-8
from collections import Iterable
import os

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
for value in d.itervalues():
    print value

# str是否可迭代
print isinstance('abc', Iterable)
# list是否可迭代
print isinstance([1, 2, 3], Iterable)
# 整数是否可迭代
print isinstance(123, Iterable)

for i, value in enumerate(['A', 'B', 'C']):
    print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

print range(1, 11)

L = []
for x in range(1, 11):
    L.append(x * x)
print L

print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11)if x % 2 == 0]
# 全排列
print [m + n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下的所有文件和目录名
print [d for d in os.listdir('.')]

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
    print k, '=', v

print [k + '=' + v for k, v in d.iteritems()]

H = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in H]

print isinstance('aaa', str)
