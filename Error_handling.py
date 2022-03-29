#TRY and EXCEPT errors handling
#we need enter the errors statments in TRY section and in except statment  we need enter what type of error

#basic
"""a=10/0
print(a)"""
#this is zerodivision error we cannot divide the number with zero it gives infinity so we need to tell
#the user your entered value is exception of operations
#Zerodivision error
#pr:1
try:
    a=10/0
    print(a)
except ZeroDivisionError:
    print(" this statement is raising an arithematic exception")
else:
    print("success")
#pr:2
try:
    a=10/2
    print(a)
except ZeroDivisionError:
    print(" this statement is raising an arithematic exception")
else:
    print("success")
#pr:3 ArithmeticError
try:
    a=10/2
    print(a)
except ArithmeticError:
    print(" this statement is raising an arithematic exception")
else:
    print("success")

#pr:4 without mentioning error
"""
try:
    a=int(input("enter the value of a :"))
    b=int(input("enter the value of b :"))
    c=a/b
    print("the division of c :",c)
except:
    print("this statement raising an arithematic exception")"""

#pr:5 lookup error orIndexError: list index out of range
"""a=[1,2,3,4]
print(a[5])"""
try:
    a=[1,2,3,5]
    print(a[6])
except LookupError:
    print("list index out of bound error")
else:
    print("success")
#key error mostly occured in dictionary function
dict={'a':1,'b':2,'c':3}
print(dict['a'])
#print(dict['d'])#KeyError: 'd'
try:
    dict = {'a': 1, 'b': 2, 'c': 3}
    print(dict['a'])
    print(dict['d'])#KeyError: 'd'
except KeyError:
    print("key error")
#class and object using try and exception method
try:
    class test:
        def division(self, a, b):
            div= a / b
            return div


    a = int(input("enter the vale of a: "))
    b = int(input("enter the value of b:"))
    divide = test()
    div=divide.division(a, b)
    print("division of given value id :", div)
except ZeroDivisionError:
    print("this statement raising an arithmetic exception")
except ValueError:
    print("this statement raising an arithmetic exception, pls enter number only")

#value error
try:
    print(int('a'))
except ValueError:
    print('value error')
try:
    class test:
        def subraction(self, a, b):
            sub= a - b
            return sub


    a = int(input("enter the vale of a: "))
    b = int(input("enter the value of b:"))
    minus = test()
    sub=minus.subraction(a, b)
    print("subraction of given value  :", sub)
except ValueError:
    print("this statement raising an arithmetic exception pls enter numbers only")
#positive or negative using functions with exceptions
try:
    def number(a):
        if (a%2==0):
            print("positive")
        else:
            print("negative")
            return a
    a=int(input("enter the number"))
    num=number(a)
    print(num)
except:
    print("value error enter the number")
finally:
    print("program completed")

















