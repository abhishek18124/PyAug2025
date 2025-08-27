arr = [10, 20, 30, 40, 50]
print(type(arr))
print(len(arr))

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

print()

print(arr[-1])
print(arr[-2])
print(arr[-3])
print(arr[-4])
print(arr[-5])

arr[0] = 1000

print(arr)

for item in arr:
	print(item, end=' ')
print()

key = 50
print(key in arr)

key = 100
print(key in arr)

l = list("python")
print(l)