def generate_subarrays(arr:list[int], n:int)->None:
	# iterate over all the possible starting indices
	for i in range(n):
		for j in range(i, n): 
			# print the subarray that starts at 
			# the ith index and ends at the jth
			# index
			for k in range(i, j+1): # [i, j+1) # [i, j]
				print(arr[k], end=' ')
			print()

arr = [10, 20, 30, 40, 50]
n = len(arr)

generate_subarrays(arr, n)