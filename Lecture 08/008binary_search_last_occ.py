import bisect

def binary_search_last_occ(nums:list[int], targ:int) -> int:
	s = 0
	e = len(nums) - 1
		
	ans = -1

	while s <= e:
		m = (s+e) // 2
		if nums[m] == targ:
			ans = m
			# reduce search sapce from [s, e] to [m+1, e]
			s = m+1
		elif targ > nums[m]:
			# reduce the search space from [s, e] to [m+1, e]
			s = m+1
		else:
			# targ < nums[m]
			# reduce the search space from [s, e] to [s, m-1]
			e = m-1
	
	return ans

nums = [10, 20, 30, 30, 30, 50, 60]
targ = 30

print(binary_search_last_occ(nums, targ))
print(bisect.bisect_right(nums, targ)) # bisect_right returns the index of the 1st element > targ
