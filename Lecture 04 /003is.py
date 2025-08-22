x = 10
y = x

print(x, id(x))
print(y, id(y))
print(x is y)

z = 10
print(z, id(z))

x = x + 1

print(x, id(x))
print(y, id(y))
print(z, id(z))

print(x is y)
print(x is not y)
