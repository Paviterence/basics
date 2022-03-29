a=["pavi","naren","haji"]
for i in range(10):
    print(",".join(a))
#add of enter value
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=a+b
sum=0
for i in range(5):
    sum=sum+c
    print(sum)
#repeat the string value
a=input("enter the value of a: ")
b=input("enter the value of b: ")
c=a+b
for i in range(5):
    print(c)
#print odd numbers
start=int(input("enter the starting range value: "))
end=int(input("enter the ending range value: "))
for i in range(start,end+1):
    if(i%2!=0):
        print(i)
#print even numbers
start=int(input("enter the starting range value: "))
end=int(input("enter the ending range value: "))
for i in range(start,end+1):
    if(i%2==0):
      print(i)

print("practice over")



