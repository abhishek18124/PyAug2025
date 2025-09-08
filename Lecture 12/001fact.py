def f(n:int)->int:
	# base case

	if n == 0:
		# find 0!
		return 1
	
	# recursive case

	# f(n) : find n factorial

	# 1. ask your friend to find n-1!

	A = f(n-1)

	return n * A


n = int(input())
print(f(n))