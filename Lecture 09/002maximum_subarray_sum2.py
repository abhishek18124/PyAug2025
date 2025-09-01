import sys

# time : n to precompute psum[] + n^2 to find maximum subarray sum ~ O(n^2)
# space: O(n) due to psum[]

def maximum_subarray_sum(arr:list[int], n:int)->int:

	psum = [None]*n # psum[i] stores the sum of the prefix ending at the ith index
	psum[0] = arr[0]
	for i in range(1, n):
		psum[i] = psum[i-1] + arr[i]

	max_so_far = -sys.maxsize-1
	for i in range(n):
		for j in range(i, n):
			# find the sum of the subarray
			# that starts at the ith index
			# and ends at the jth index 
			s = psum[j] if i == 0 else psum[j] - psum[i-1]
			max_so_far = max(max_so_far, s)

	return max_so_far

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)

print(maximum_subarray_sum(arr, n))