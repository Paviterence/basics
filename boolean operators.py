print("boolean operator or,and,not")
# or operator
definition='''when you use or it will return the 1st value if the expression is true, 
else it will blindly return the second value'''
print(definition)
def or_(a,b):
    if a>b:
        return a
    else:
        return b
c=or_(6,5)
print(c)
def and_(a,b):
    if a<b:
        return a
    else:
        return b
c=and_(6,5)
print(c)


x=True
y=False
z=x or y
print(z)
x=True
y=True
z=x or y
print(z)
x=False
y=False
z=x or y
print(z)
x=False
y=True
z=x or y
print(z)
#and operator
defi='''{and}evaluates second arguments if both arguments are truth.otherwise evaluates to the 1st falsey argument'''
print(defi)
x=True
y=False
z=x and y
print(z)
x=True
y=True
z=x and y
print(z)
x=False
y=False
z=x and y
print(z)
x=False
y=True
z=x and y
print(z)
#not it gives opposite of following statement
print("not statement")
x=True
y=not x
print(y)
x=False
y=not x
print(y)