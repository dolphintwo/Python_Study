# coding: utf-8
# 切片

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print L

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print [L[0], L[1], L[2]]

r = []
n = 3
for i in range(n):
    r.append(L[i])
print r

# 切片
print L[0:3]
# 前闭后开
print L[1:3]
# 倒数切片
print L[-2:]
print L[-2:-1]

L = range(100)
print L
print L[:10]
print L[-10:]
print L[10:50:3]
print L[:]

print (0, 1, 2, 3, 4, 5, 6)[:3]

# 字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符
print 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:26:3]
print 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[::2]
