#inheritance two methods are ther 1)has a-->tightly coupled,composition 2)is a__> loosly coupled parent child
#relation,reusing the parent calss function
#is a method in inheritence
#basic programs using parent child

"""class aircraft:
    def __init__(self,name,length,height,model):
        self.name=a
        self.length=b
        self.height=c
        self.model=d
class spl_specs(aircraft):
    def __init__(self, size, range, engine, height):
        self.size=size
        self.range=range
        self.engine=engine
        super().__init__(a,b,c,d,size,range,engine)
    def __str__(self):
        return 'name:{}\n,lenghth:\n,height:\n,spanlength:\n,size:\n,range:\n,engine:\n'.format(self.name,self.length,
        self.model,self.size,self.range,self.engine)
ac1=spl_specs("boeing","240m","50m","737","narrowbody","5000knots","twin spool")
print(ac1)"""
'''
class android_09:
    def v1(self):
        print("navigation bar updated")
        print("music quality updated")
        print("video quality updated")
class android_10(android_09):
    def v2(self):
        print("display quality improved")
        print("outdoor brightness enhanced")
class android_11(android_10):
    def v3(self):
        samsung.v1()
        samsung.v2()
        print("security level improved")
        print("maps navigation improved")
samsung = android_11()
samsung.v3()'''


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(person):
    def __init__(self,name,age,empid,salary):
        super().__init__(name,age)
        self.empid=empid
        self.salary=salary
    def __str__(self):
        return 'name={}\nsalary={}\n'.format(self.name,self.salary)
emp1=Employee("pavi",24,1725,40000)
print(emp1)
#multilevel inheritance
class GrandParent:
    def agriculture(self):
        print("watering plants")
class parent(GrandParent):
    def readingbooks(self):
        print("reading books")
class child(parent):
    def programming_(self):
        print('practicing python programming regularly')

c = child()
c.programming_()
c.readingbooks()
c.agriculture()

#multiple inheritance
#two parent class one child class
class father:
    def work_(self):
        print("my father is a pilot, so i am")
class mother:
    def work_(self):
        print("my mother is doctor, so i am")
class child(father,mother):
    def studying(self):
        print("i am studying now")
c=child()
c.studying()
c.work_()