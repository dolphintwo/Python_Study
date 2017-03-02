# -*- coding: utf-8 -*-
# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict。


def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

print person('Michael', 30)
print person('Bob', 35, city='Beijing')
print person('Adam', 45, gender='M', job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}
print person('Jack', 24, city=kw['city'], job=kw['job'])


# 参数组合
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
print func(1, 2)
print func(1, 2, c=3)
print func(1, 2, 3, 'a', 'b')
print func(1, 2, 3, 'a', 'b', x=999)


args = (1, 2, 3, 4)
kw = {'x': 99}
print func(*args, **kw)

# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。