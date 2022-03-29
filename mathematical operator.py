#division
import math
a,b,c,d,e=5,2,3,2,1
#a=int(input("enter a="))
#b=int(input("enter b="))
#c=int(input("enter c="))
#d=int(input("enter d="))
#e=int(input("enter e="))
print("division is:",a/b)
print("quotient is:",a//b)
print("reminder is:",a%b)
print("a/c:",a/c)
print("a/c:",d/e)
print("c/d:",c/d)
print("c/a:",c/a)
print("a/e:",a/e)
#operator
import operator
#operator.div(a,b)
#perator.__div__(a,b) function
print("=================done===================")
#addition
print("addition is:",a+b)
a +=b#increment addition operator
print("addition is:",a)
str1=[1,2,3]#concatenation of string
str2=[4,5,6]
print("str list concatenation is:",str1+str2)
str1=(1,2,3)#concatenation of string
str2=(4,5,6)
print("str tuple concatenation is:",str1+str2)
print("=================done===================")
#exponentiation
a,b=8,2
print("a square is b or a power b is:",a**b)
c=pow(a,b)
print("pow keyword:",c)
a,b,c=8,2,5
print("quotient:",(a**b)//c)
print("square with modules or ((a**b)%c=reminder) :",pow(a,b,c))
print("=================done===================")
#square root
import math
a=4#always float do not allow complex result
math.sqrt(a)
print(math.sqrt(a))
x=8
print("cube root of x:",x**(1/3))#for cube root
print("=================done===================")
#exponentital
import math
print(math.exp(0))
print(math.exp(1))
print(math.exp(2))
print(math.exp(-3))
print(math.exp(1e-6))
print(math.exp(1e-3))
print(math.exp(10e-3))
print(math.exp(10e-1))
print("=================done===================")
#inplace operation "="--> character makes in place operation
a=8
#a=a+1
a+=1
print(a)
#a=a-1,a=a*1,a=a/1,a=a//1,a=a%1,a=a**1,a=a+1,a=a-1
a-=1
print(a)
a*=1
print(a)
a**=2
print(a)
a//=5
print(a)
a%=5
print(a)
print("=================done===================")
#print multiplication
a,b=2,5
print(b*a)
print("'*'operator is used to repeated concatenation of string,list,and tuples")
a=(1,2)*3
print(a)
print("=================done===================")
#modulus
explanation='''the modulus operator gives reminder value of the given vale
you can give negative numbers also
if you want  quotient and reminder we have to you divmod for getting the value'''
print(explanation)
a=-9%7
b=9%7
print(a)
print(b)

quotient,reminder=divmod(9,4)
print("quotient= ",quotient,"reminder=",reminder)
#operator mode
import operator
print(operator.mod(10,2))#10%2
print(operator.mod(15,2))
print(operator.mod(10,20))
print("=================done===================")










