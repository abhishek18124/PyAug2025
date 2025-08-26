arr = (10, 20, 30, 40, 50)
print(type(arr))
print(arr)

# arr[0] = 1000 # tuple are immutable

print(arr[0], end=' ')
print(arr[1], end=' ')
print(arr[2], end=' ')
print(arr[3], end=' ')
print(arr[4])
# print(arr[5]) # IndexError

print()

for item in arr:
	print(item, end=' ')
print()

print(arr[-1], end=' ')
print(arr[-2], end=' ')
print(arr[-3], end=' ')
print(arr[-4], end=' ')
print(arr[-5])
# print(arr[-6]) # IndexError


brr = (100,) # w/o , brr will point an int obj with value 100
print(type(brr))

s = "coding"
t = tuple(s)
print(type(t))
print(t[0], end=' ')
print(t[1], end=' ')
print(t[2], end=' ')
print(t[3], end=' ')
print(t[4], end=' ')
print(t[5])
print(t)

for ch in t:
	print(ch, end=' ')
print()

