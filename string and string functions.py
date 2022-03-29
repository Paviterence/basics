#string function
import string

name="pavithrabalan sethu"
print(name)
print(type(name))
print(id(name))
print(dir(name))
print(len(name))
print("-------")
print(name.endswith("u"))
print("-------")
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[0:4])
print(name[8:13])
print(name.index("p"))
print(name.index("a"))
print(name.index("v"))
print(name.index("i"))
print(name.capitalize())
print(name.center(50))
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.isnumeric())
letters=string.ascii_uppercase
print((',').join(letters))
print(tuple(letters))
print(list(letters))
print(set(letters))






