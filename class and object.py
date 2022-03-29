class supermarket:
    discount=0.04
product1= supermarket()
product2= supermarket()
print(product1)
print(product2)
product1.name="soap"
product1.price=20
product2.name="shaampoo"
product2.price=10
print(product1.name)
print(product1.discount)


class supermarket:
    specialdiscount="10%"
    def __init__(self,name,price,discount):
        self.name=name
        self.price=price
        self.discount=discount

product1=supermarket("dairymilk",100,"2%")
product2=supermarket("bournvile",150,"1.5%")
print(product1.name)
print(product1.price)
print(product1.discount)
print(product1.specialdiscount)
print("\n",product2.name)
print(product2.price)
print(product2.discount)
print(product2.specialdiscount)
#with return
class supermarket:
    specialdiscount="10%"
    def __init__(self,name,price,discount):
        self.name=name
        self.price=price
        self.discount=discount
    def product_details(self):
        #return '{}- {} - {}'.format(self.name,self.price,self.discount,self.specialdiscount)
        return self.name, self.price,self.discount,self.specialdiscount

product1=supermarket("dairymilk",100,"2%")
product2=supermarket("bournvile",150,"1.5%")
#print(product1.product_details())
#print(product2.product_details())
print(supermarket.product_details)
#dog details
class dog:
    animal="dog"
    def __init__(self,breed,color):
        self.breed=breed
        self.color=color
    def dog_details (self):
            return self.breed,self.color,self.animal
    def __str__(self):
        return "breed={}/n - color={}".format(self.breed,self.color,self.animal)

domi=dog("pug","brown")
briyaan=dog("germanshepard","brown")
print(domi.dog_details())
print(briyaan.dog_details())
print(dog.dog_details(domi))
print(dog.dog_details(briyaan))
#addition
class test:
    def addition(self,a,b):
        add=a+b
        return add

a=int(input("enter the vale of a: "))
b=int(input("enter the value of b:"))
plus=test()
add=plus.addition(a,b)
print("addition is :",add)

