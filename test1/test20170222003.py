# coding: utf-8
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# print my_abs(-10, 9)
# print my_abs('A')
# print abs('A')


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y
