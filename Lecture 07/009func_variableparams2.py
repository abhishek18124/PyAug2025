def add(a, b, *c):
	print(a, b, c)
	print(type(a), type(b), type(c))
	return a + b + sum(c)

print(add(2, 3, 5))
print(add(2, 3, 5, 6))
print(add(2, 3, 5, 6, 7))