def generate_pairs(arr:list[int], n:int)->None:
	for i in range(0, n-1): # [0, n-1) # [0, n-2]
		for j in range(i+1, n): # [i+1, n) # [i+1, n-1]
			print(arr[i], arr[j])
		print()

arr = [10, 20, 30, 40, 50]
n = len(arr)

generate_pairs(arr, n)