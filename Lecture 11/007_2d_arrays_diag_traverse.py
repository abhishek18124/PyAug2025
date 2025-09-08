def print_diagonal(nums:list[list[int]], m:int, n:int, i:int, j:int)->None:

	# print the diagonal that start at the i,jth index

	while i <= m-1 and j <= n-1:
		print(nums[i][j], end=' ')
		i += 1
		j += 1

	print()

nums = [[11, 12, 13, 14], 
		[15, 16, 17, 18], 
		[19, 20, 21, 22]]

m = len(nums)
n = len(nums[0])

# (0, 0), (0, 1), (0, 2), ... (0, n-1) => (0, j) where 0<=j<=n-1

for j in range(n):
	print_diagonal(nums, m, n, 0, j)

# (1, 0), (2, 0), (3, 0), ... (m-1, 0) => (i, 0) where 1<=i<=m-1
for i in range(1, m):
	print_diagonal(nums, m, n, i, 0)
