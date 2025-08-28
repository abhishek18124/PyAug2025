def binary_search(nums:list[int], targ:int) -> int:
	s = 0
	e = len(nums) - 1
	
	while s <= e:
		m = (s+e) // 2
		if nums[m] == targ:
			return m
		elif targ > nums[m]:
			# reduce the search space from [s, e] to [m+1, e]
			s = m+1
		else:
			# targ < nums[m]
			# reduce the search space from [s, e] to [s, m-1]
			e = m-1
	
	# targ not found
	return -1

nums = [10, 20, 30, 40, 50, 60]
targ = 100

print(binary_search(nums, targ))