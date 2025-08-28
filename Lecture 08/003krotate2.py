arr = [10, 20, 30, 40, 50, 60, 70]
n = len(arr)

k = 3

k = k%n # handles cases when k exceeds n

# 1. reverse the entire array arr[0...n-1]

i = 0
j = n-1

while i < j:
	arr[i], arr[j] = arr[j], arr[i]
	i += 1
	j -= 1

# 2. reverse the 1st k values arr[0...k-1]

i = 0
j = k-1

while i < j:
	arr[i], arr[j] = arr[j], arr[i]
	i += 1
	j -= 1


# 3. reverse the last n-k values arr[k...n-1]

i = k
j = n-1

while i < j:
	arr[i], arr[j] = arr[j], arr[i]
	i += 1
	j -= 1


print(arr)