#list with letters
import string
letters=string.ascii_uppercase[:26]
print(letters)
print(' ,'.join(letters))
alpha=list(letters)
print(alpha)
print(len(alpha))
print(type(alpha))
print(alpha[0],alpha[14],alpha[25],alpha[1],alpha[16])
alpha[0]="pavi"
alpha[14]="kani"
alpha[25]="dharu"
alpha[1]="haji"
alpha[16]="sethu"
print(alpha)
print(alpha.index("C",))
alpha.append("append added")
alpha.append("append added again")
print(alpha)
alpha.extend('extend')
print(alpha)
print(len(alpha))
print(alpha.index("e",28,34))# index
alpha.insert(28,"i am inserted")
print(alpha)
print(alpha[20],alpha[30])
alpha.insert(20,"before u")
print(len(alpha))
alpha[30]="pavi"
print(alpha)
#list remove function
hi=alpha
print(hi)
hi.remove("pavi")
hi.remove("pavi")
print(hi)
del hi[0]
print(hi)
print(len(hi))
del hi[32:34]
print(hi)
print(hi.pop(0))
print(hi.pop())
print(hi.pop(-1))
print(hi.pop(-10))
print(hi.pop(-25))
print(len(hi))
hi.remove("i am inserted")
print(hi)
del hi[0:20]
print("\n",hi)
print(len(hi))
del hi[:6]
print("\n",hi)
print("\n letters with using list fuction insert,append,replace,index value,remove,del,pop,clr,join,len commands practice done here")