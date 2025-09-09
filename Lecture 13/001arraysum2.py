def f(x:list[int], n:int, i:int)->int:
	# base case

	if i == n:
		# find the sum of x[n...n-1] = []
		return 0

	# recursive case

	# f(i) = find the sum of x[i...n-1]

	# ask your friend to find the sum of x[i+1...n-1]

	A = f(x, n, i+1)

	return x[i] + A

n = int(input())
x = list(map(int, input().split()))
print(f(x, n, 0))