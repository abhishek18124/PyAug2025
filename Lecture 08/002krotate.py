arr = [10, 20, 30, 40, 50, 60, 70]
n = len(arr)

k = 3

# time : O(kn)

for _ in range(k):
	for i in range(n-1, 0, -1): # start = n-1 stop = 0 step = -1 # [n-1, 0)
		arr[i], arr[i-1] = arr[i-1], arr[i]


print(arr)