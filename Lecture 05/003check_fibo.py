n = int(input())
if n == 0 or n == 1:
	print(True) # n is a fib. no.
else:
	a = 0 # 0th fib. no.
	b = 1 # 1st fib. no.

	while True:
		c = a + b
		if c == n:
			print(True)
			break

		if c > n:
			print(False)
			break

		# c < n

		a = b
		b = c