def add(a: int, b: int, c: int) -> int:
	print(a, b, c)
	return a + b + c

print(add(2, 3, 5))

print(add(b=3, c=5, a=2))