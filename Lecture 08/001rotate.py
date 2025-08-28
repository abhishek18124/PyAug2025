arr = [10, 20, 30, 40, 50]
n = len(arr)

# time : O(n)

for i in range(n-1, 0, -1): # start = n-1 stop = 0 step = -1 # [n-1, 0)
	arr[i], arr[i-1] = arr[i-1], arr[i]

print(arr)