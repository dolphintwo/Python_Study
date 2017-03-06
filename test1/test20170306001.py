# -*- coding: utf-8 -*-
from random import choice
import math

print 'abc'.count('a')
x = choice(['Hello World!', [1, 2, 'e', 'e', 4]])
print x.count('e')


def add(x, y, f):
    return f(x) + f(y)
print add(25, 9, math.sqrt)


def f(x):
    return x * x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def format_name(s):
    return s[0].upper() + s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])


def is_odd(x):
    return x % 2 == 1
print filter(is_odd, [1, 2, 3, 4, 5, 6, 7])


def is_not_empty(s):
    return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', None, '', 'str', ' ', 'END'])


a = '           123'
print a.strip()
a = '\t\n\r123\r'
print a
print a.strip()


def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r == x
print filter(is_sqr, range(1, 101))

print sorted([45, 23, 21, 45, 78, 1])


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([45, 23, 21, 45, 78, 1], reversed_cmp)

print sorted(['bob', 'about', 'Zoo', 'Credit'])


def cmp_ignore_case(s1, s2):
    if s1.lower() > s2.lower():
        return 1
    if s1.lower() < s2.lower():
        return -1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
