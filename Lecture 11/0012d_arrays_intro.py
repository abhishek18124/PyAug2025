nums = [[10, 20], [30, 40], [50, 60]]
print(nums)
print(nums[0][0])
print(nums[0][1])
print(nums[1][0])
print(nums[1][1])
print(nums[2][0])
print(nums[2][1])

m = int(input()) # rows
n = int(input()) # cols

nums = [[0]*n for _ in range(m)]