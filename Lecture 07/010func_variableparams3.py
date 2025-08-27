def add(a, *b, c):
	print(a, b, c)
	print(type(a), type(b), type(c))
	return a + sum(b) + c
	
print(add(2, 3, 5, 6, c=7))