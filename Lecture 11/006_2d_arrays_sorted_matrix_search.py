# time : O(m+n)
# space: O(1)
def is_present(nums:list[list[int]], target:int)->bool:
	
	m = len(nums)
	n = len(nums[0])

	i = 0
	j = n - 1

	while i <= m-1 and j >= 0:
		if nums[i][j] == target:
			return True
		elif target > nums[i][j]:
			i += 1
		else:
			# target < nums[i][j]
			j -= 1

	return False # target was not found

nums = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
target = 70

print(is_present(nums, target))