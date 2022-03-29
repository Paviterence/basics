"""def wish(greetings):#formal arguments
    print("hello")
    print("i am practicing python functions")
    print("wish me good luck to become a good programmer")
wish("hi")#actual arguments

def wish():
    print("hello")
    print("i am practicing python functions")
    print("wish me good luck to become a good programmer")
wish()

def welcome(name):
    print("hello" +str(name))
    print("hello",name)
    print(name,"is  practicing python functions")
    print(" good luck",name,"to become a best programmer")
name=(input("enter your name: "))
#name=wish(input("enter your name"))
welcome(name)
#using loop
def welcome(name):
    print("hello",name)
    print(name,"is  practicing python functions")
    print("good luck",name,"to become a best programmer")
count=1
while count<=10:
    n = int(input("enter how many persons to welcome"))
    name = (input("enter your name: "))
    # name=wish(input("enter your name"))
    welcome(name)
    count+=1# it means count-->count=count+1

def welcome(name):
    print("hello",name)
    print(name,"is  practicing python functions")
    print("good luck",name,"to become a best programmer")
count=1
n=int(input("enter number of  person to welcome:  "))
while count<=n:
    name = (input("enter your name: "))
    # name=wish(input("enter your name"))
    welcome(name)
    count+=1# it means count = count=count+1

#return
def squareOfNumber(num):
    return num*num
#num=int(input("enter the number"))
#result=squareOfNumber(num)
result=squareOfNumber(int(input("enter the number: ")))
print(result)
#additon
def addition(num1,num2):
    return num1+num2
result=addition(10,20)#assignment operators
print(result)
#print(addition(10,20))#positional arguments

def addition(num1,num2):
    return num1+num2
num1=int(input("enter number1 :"))
num2=int(input("enter number 2: "))
print(addition(num1,num2))
#result=addition(num1,num2)#assignment operators
#print(result)
#calculator
def calculator(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    rem=a%b
    return add,sub,mul,div,rem
    #return "add={}, sub={}, mul={}, div={}, rem={}".format(add,sub,mul,div,rem)
a=int(input("enter a: "))
b=int(input("enter b: "))
result=calculator(a,b)
print(result)
print(type(result))#tuple value
for x in result:#to get separate values
    print(x)
#key word arguments example
def sub(num1,num2):
    return num1-num2
result=sub(num2=100,num1=20)#its not working based on position its working based on the key word 20-100=-80
#result=addition(num1=10,num2=20)#assignment operators
print(result)
#example
def welcome(name,msg):
    print("hi",name,msg)
welcome("haji","naren")
#welcome(name="naren",haji)__>SyntaxError: positional argument follows keyword argument
#welcome("naren",name="haji")-->TypeError: welcome() got multiple values for argument 'name'positional argument follows
welcome(msg="naren",name="haji")#keywords changed
#default arguments here position and  key arguments applicable in actual arguments place
def welcome(name="admin"):
    print("hi", name)
welcome("pavi")
welcome()#if you not give any arguments its print default arguments
def supermarket(discount=10):
    print(discount)
supermarket()#default discount for all products in super market
supermarket(20)#this product have 20% discount so function will prints this also
#variable length arguments
#syntax(*n): example its used for university to save students marks and data
def caltotal(*n):#single star for store tuple value
    total=0
    for subject in n:
        total=total+subject
    print(total)
caltotal()
caltotal(90)
caltotal(60,50,80)
caltotal(50,50,50,50)
#dictionary arguments,keys and valus syntax(**kwargs)
def studentdata(**kwargs):
    for sub,mark in kwargs.items():
        print("subject:",sub,"scored mark:",mark)
studentdata(tamil=50)
studentdata(tamil=50,english=60)
studentdata(tamil="fifty",english="hundred")"""
#notes
"""function-group of instruction with a name
module-group of modules saved to a file
library-group pf modules"""
#global variable mentioned above function
#local variable within function
discount=40#local variable
def purchaseTV():
    #global discount if you mention global variable inside the function just mention before variable global
    #discount=60
    print("tv",discount)
def purchaselaptop():
    print("laptop:",discount)

def purchasedress():
    discount=40#local variable
    print("g.dis",globals()["discount"])#using this syntax you can add global variable also in function
    print("dress:",discount)
purchaseTV()
purchaselaptop()
purchasedress()




