nums = [[10, 20], [30, 40], [50, 60]]
nums_copy = nums[:]


print(nums)
print(nums_copy)

nums_copy[0][0] = 100

print(nums_copy)

print(nums)