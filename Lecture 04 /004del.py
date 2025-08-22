x = 10
print(x, id(x))
# del x
# print(x)
y = 20
z = y
print(y, id(y))
print(z, id(z))
print(y is z)
del y
print(z)