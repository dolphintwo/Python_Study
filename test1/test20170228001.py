# -*- coding: utf-8 -*-
# 关键字参数


def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

print person('Michael', 30)
print person('Bob', 35, city='Beijing')
print person('Adam', 45, gender='M', job='Engineer')
