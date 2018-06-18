'''

name = "hello"
tuples = ("hello")
print(len(tuples))
l = [1,23,3]
print(tuple(l))



a = set([1,2,3])
b = set([3,4,5])
print(a&b)
print(a|b)

a = set()
a.add("hello")
print(a)
a.update([1 , 2 , 3])
print(a)
a.pop()
print(a)
s = set((1,2,3))
s.remove(2)
s.discard(2)
print(s)

a = set([1,2,3,4,5])
b = set([3,4,5])
print(a>=b)
'''

d = { 'name' : 'rahul' ,
     'age' : 9
     }

print(d['age'])
d['name'] = "xyz"
print(d)
del d['name']
print(d)
d.clear()
print(d)
del d
print(d)