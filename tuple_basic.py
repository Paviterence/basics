#tuple practice
a="boeing","airbus"
print(a)
a=list(range(10))
print(a)
b=tuple(a)
print(b)
#cocatenation of tuple
a1="boeing","airbus"
b1=0, 1, 2, 3, 4, 5, 6, 7, 8, 9
c=(a1+b1)
print(c)
print(a1,b1)#nesting of tuple
print(a,b)
print(c,a)
#repetition in tuples
a=("python",)*5
print(a)
b=(1,2,3,4,5,6,7,8,9,10)*2
print(b)
print(a,b)
#tuples are  immutable so we can't  replace any value in tuples
h=list(range(50,1,-2))
print(tuple(h))
print(len(h))
print(h[1:])#slicing of tuples
print(h[:20])
print(tuple(h[::-1]))
hello=(0,1,2,3)
print(hello[::-1])
print(hello)
my_name=input("enter you name:")
n=int(input("enter number of time to repeat your name :"))
for i in range(int(n)):
    print(my_name)




