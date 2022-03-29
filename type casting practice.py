#type casting

a=10.0
print(a)
print(type(a))
b=int(a)
print(b)
print(type(b))

a=input("enter the value of a: ")
b=input("enter the value of b: ")
c=a+b
print(c)
print(type(c))# in input method all values are always consider as a string
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=a+b
print("total",c)
print("total: "+str(c))#whenever you add + you need to mention str
print(type(c))

a=float(input("enter the value of a: "))
b=float(input("enter the value of b: "))
c=a+b
print("total",c)
print("total: "+str(c))#whenever you add + you need to mention str
print(type(c))
d=int(c)
print(d)
print("type casting program practice ended")