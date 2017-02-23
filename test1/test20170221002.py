# -*- coding: utf-8 -*-
# set

s = set([1,2,3])
print s

s = set([1,3,4,2,2,4,1])
print s

s.add(8)
print s

s.remove(4)
print s

s1 = set([1,2,3])
s2 = set([2,3,4])
print s1 & s2
print s1 | s2

a = ['c', 'b', 'a']
print a
a.sort()
print a

a = 'abc'
print a.replace('a', 'A')
print a
