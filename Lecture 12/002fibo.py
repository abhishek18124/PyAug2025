def f(n:int)->int:
	# base case
	if n == 0 or n == 1:
		return n

	# recursive case

	# f(n) = find the nth fibo. no.

	# 1. ask your friend to find the n-1th fibo. no.

	A = f(n-1)

	# 2. ask your friend to find the n-2th fibo.no.

	B = f(n-2)

	return A + B


n = int(input())
print(f(n))