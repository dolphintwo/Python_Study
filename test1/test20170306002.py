# coding: utf-8
# 函数中返回函数


def f():
    print 'call f()...'
    # 定义函数g:

    def g():
        print 'call g()...'
    # 返回函数g:
    return g


def myabs():
    return abs
    # 返回函数


def myabs2(x):
    return abs(x)
    # 返回函数调用的结果，返回值是一个数值


def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum

f = calc_sum([1, 2, 3, 4])
print f
print f()


def prod(x, y):
    return x * y

print reduce(prod, [2, 4, 5, 7, 12])