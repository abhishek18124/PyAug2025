# time : O(n)
# space: O(n) due to fn call stack

def f(n:int)->None:
	# base case
	if n == 0:
		return

	# recursive case

	# f(n) : print nos. from 1 to n in the inc. order

	# 1. ask your friend to print nos. from 1 to n-1 in the inc. order

	f(n-1)

	print(n, end=' ')

n = int(input())
f(n)