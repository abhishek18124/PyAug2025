nums = [[10, 20, 30],
		[40, 50, 60],
		[70, 80, 90]]

m = 3
n = 3

for j in range(n):
	if j%2 == 0:
		# print the jth column top to bottom
		for i in range(m):
			print(nums[i][j], end=' ')
	else:
		# print the jth column bottom to top
		for i in range(m-1, -1, -1):
			print(nums[i][j], end=' ')