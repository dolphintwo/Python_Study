# coding: utf-8


def power(x):
    return x * x

print power(5)
print power(15)

# 默认参数 n=2


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5, 2)
print power(5, 3)
print power(5, 4)

print power(5)


def enroll(name, gender):
    print 'name:', name
    print 'gender:', gender

enroll('Sarah', 'F')


def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]
# 因为默认参数L也是一个变量，它指向对象[]
# 每次调用该函数，如果改变了L的内容，则下次调用时
# 默认参数的内容就变了，不再是函数定义时的[]了。
# 默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L
print add_end([1, 2, 3])
print add_end(['x', 'y', 'z'])
print add_end()
print add_end()


# 正确示例
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print add_end([1, 2, 3])
print add_end(['x', 'y', 'z'])
print add_end()
print add_end()


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# print calc([])
print calc([1, 2, 3])
print calc([1, 3, 5, 7])


# 可变参数
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。
# 参数numbers接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc()
print calc(1, 2, 3)
print calc(1, 3, 5, 7)


nums = [1, 2, 3]
print calc(*nums)
print calc(nums[0], nums[1], nums[2])
