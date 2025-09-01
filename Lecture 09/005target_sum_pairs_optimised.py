# time : O(n)
# space: O(1)

def target_sum_pair(arr:list[int], n:int, t:int)->int:
	cntr = 0
	i, j = 0, n-1
	while i < j:
		pair_sum = arr[i] + arr[j]
		if pair_sum == t:
			cntr += 1
			i += 1
			j -= 1
		elif pair_sum > t:
			j -= 1
		else:
			# pair_sum < t
			i += 1
	return cntr

arr = [10, 20, 30, 40, 50]
n = len(arr)
t = 60
print(target_sum_pair(arr, n, t))