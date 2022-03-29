#type 1 exception with comments
try:
    age=int(input("enter your age:"))
    if age<18:
        raise Exception
    else:
        print("permitted for voting")
except:
    print("age should be less than 18")
#type 2 raise with comments
try:
    age=int(input("enter your age:"))
    if age<18:
        raise ValueError("age should be less than 18")
    else:
        print("permitted for voting")
except ValueError as h:
    print(h)

#type 3 without try and exception it gives the error
"""
age=int(input("enter your age:"))
if age < 18:
    raise ValueError("age should be less than 18")
else:
    print("permitted for voting")"""

#type 4 using class and object raise with comments
class humantemprature:
    def __init__(self,temp):
        self.temp=temp
    def check_temp(self):
        if  self.temp >97:
            #print("you are suffering from fever")
            raise Exception("temprature abnormal")
        elif self.temp<88:
            #print("you are suffering from cold fever")
            raise Exception(" temprature abnormal")
        else:
            print('you are normal cheerup')
check=humantemprature(int(input("enter the temp: ")))
check.check_temp()


