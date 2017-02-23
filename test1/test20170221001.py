# -*- coding: utf-8 -*-
# dict Python内置了字典：dict的支持，dict全称dictionary
# 在其他语言中也称为map，使用键-值（key-value）存储
# 具有极快的查找速度。
d = {'Michael': 95, 'Bob': 85, 'Tracy': 75}
print d['Michael']

d['Adam'] = 67
print d

d['Jack'] = 80
print d

# KeyError: 'Happy',Traceback (most recent call last):
# print d['Happy']

print 'Adam' in d
print 'Happy' in d

print d.get('Adam')
print d.get('Happy', -1)

# 删除一个键值
print d.pop('Jack')
print d
