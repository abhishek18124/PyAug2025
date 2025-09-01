import sys

# time : O(n^3)
# space: O(1)

def maximum_subarray_sum(arr:list[int], n:int)->int:
	max_so_far = -sys.maxsize-1
	for i in range(n):
		for j in range(i, n):
			# find the sum of the subarray
			# that starts at the ith index
			# and ends at the jth index 
			s = 0
			for k in range(i, j+1):
				s += arr[k]
			max_so_far = max(max_so_far, s)

	return max_so_far

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)

print(maximum_subarray_sum(arr, n))