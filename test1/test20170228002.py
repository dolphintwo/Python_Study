# coding: utf-8
# 递归函数


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(10)
# 栈溢出
# print fact(1000)


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print fact(5)
# 栈溢出
# print fact(1000)

