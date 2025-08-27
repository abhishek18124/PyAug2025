def reverse_array(nums:list[int])->None:
	i = 0
	j = len(nums) - 1
	while i < j:
		nums[i], nums[j] = nums[j], nums[i]
		i += 1
		j -= 1

n = int(input())
nums = [int(input()) for _ in range(n)]
print(nums)
reverse_array(nums)
print(nums)