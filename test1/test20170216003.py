# list
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0]
print classmates[1]
print classmates[2]
# IndexError: list index out of range
# print classmates[3]

classmates.append('Adam')
print classmates

classmates.insert(1, 'Jack')
print classmates

classmates.pop(2)
print classmates

classmates[1] = 'Sarah'
print classmates

L = ['Apple', 123, True]
s = ['Python', 'Java', ['asp', 'PHP'], 'scheme']
print s
print len(s)
print s[2][1]

classmates2 = ('Michael', 'Bob', 'Tracy')
print classmates2

# tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t
