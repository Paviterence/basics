l=list(range(5))
print(l)
print(l[0])
print(l[4])
print(l[2])
l.append(5)# append
l.append(6)
l.append("pavi")
print(l)
print(l[-1])
print(l)
#extend
l.extend([10,20,30])
print(l)
l.extend(["a","b"])# its a string
print(l)
l.extend(['hello'])
print(l)
#insert function
l.insert(0,"hi")# insert syntax(index location,value)
print(l)
l.insert(-1,"hi")
print(l)
print(len(l))
l[1]="hi"
print(l)
#slice function
l[1:1]=[1,2]
print(l)
#list in remove(),clear(),del(),pop()
print(l)
l.remove("hi")
print(l)
l.remove("hello")
print(l)
l.remove("hi")
print(l)
print(l.pop(-1))
print(l.pop(-2))
print(l.pop(-3))
print(l.pop(-4))
print(l)
del l[1]
del l[0]
del l[-1]
del l[-2]
print(l)
del l[-1]# syntax for delete del l[start:stop]
print(l)
del l[-2:]
print(l)
l.insert(0,0)
print(l)
l.clear()
print(l)


