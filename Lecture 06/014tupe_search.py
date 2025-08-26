def search(nums:tuple, key:int)->bool:
	for num in nums:
		if num == key:
			return True
	return False

nums = [10, 20, 30, 40, 50]
key = 20

# print(search(nums, key))

print(key in nums)

key = 100

print(key in nums)