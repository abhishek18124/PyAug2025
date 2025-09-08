def f(x:int, y:int)->int:
	# base case
	if y == 0:
		# find x * 0
		return 0

	# recursive case

	# f(x, y) : find x * y

	# 1. ask your friend to find x * (y-1)

	A = f(x, y-1)

	return x + A

x = int(input())
y = int(input())
print(f(x, y))