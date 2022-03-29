import string
letters=string.ascii_lowercase[:6]
print(letters)
print(','.join(letters))
test=set(letters)
print(test)
test.add("f")
print(test)
test.remove("a")
print(test)
print(len(test))
print(test)
print(test)
