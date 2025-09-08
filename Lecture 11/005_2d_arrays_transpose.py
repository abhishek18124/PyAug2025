nums = [[11, 12, 13, 14],
		[15, 16, 17, 18],
		[19, 20, 21, 22],
		[23, 24, 25, 26]]

# time : O(n^2)

n = 4

for i in range(n):
	for j in range(i+1, n):
		nums[i][j], nums[j][i] = nums[j][i], nums[i][j]

for i in range(n):
	for j in range(n):
		print(nums[i][j], end=' ')
	print()
print()