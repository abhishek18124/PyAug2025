n = int(input())

if n == 0 or n == 1:
	print(n)
else :
	# n >= 2
	a = 0 # 0th fib. no.
	b = 1 # 1st fib. no.

	i = 1

	while i <= n-1:
		c = a + b
		a = b
		b = c
		i = i + 1

	print(c) # print(b) # both b and c hold the nth fib. no.

# time : (n-1).const ~ O(n)
# space: O(1)