# time : O(n^2)
# space: O(1)

def target_sum_pair(arr:list[int], n:int, t:int)->int:
	cntr = 0
	for i in range(0, n-1):
		for j in range(i+1, n):
			pair_sum = arr[i] + arr[j]
			if pair_sum == t:
				cntr += 1
	return cntr

arr = [10, 20, 30, 40, 50]
n = len(arr)
t = 60
print(target_sum_pair(arr, n, t))