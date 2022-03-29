#function with return value
#basic program
def add(a,b):
    c=a+b
    return c

x=add(1,2)
print(x)
#additiob subraction multiplication
def add_(a,b):
    return (a+b)

def sub_(a,b):
    return (a-b)

def multi_(a,b):
    return (a*b)

x=add_(1,2)
print("result of add_ function : ",x)
x=sub_(2,3)
print("\nresult of sub_ function : ",x)
x=multi_(4,6)
print("\nresult of multi_ function : ",x)

#addition and boolean
def add(a,b):
    return a+b

def is_true(a):
    return bool(a)
result=add(2,3)
print("result of add function : ",result)
res=is_true(2<5)
print("\nresult of is_true function",result)
