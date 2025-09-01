import sys

# time : O(n)
# space: O(1) 

def maximum_subarray_sum(arr:list[int], n:int)->int:
	
	x = arr[0] # x represents x[0] init
	max_so_far = x

	for i in range(1, n):
		x = max(x + arr[i], arr[i])
		max_so_far = max(max_so_far, x)

	return max_so_far



arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)

print(maximum_subarray_sum(arr, n))