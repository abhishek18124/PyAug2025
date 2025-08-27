nums = [] # empty list
n = int(input())
for _ in range(n):
	item = int(input())
	nums.append(item)
print(nums, len(nums))

nums2 = list(map(int, input().split()))
print(nums2, len(nums2))

# "100 200 300 400 500" => ["100", "200", "300", "400", "500"] => [100, 200, 300, 400, 500]

nums3 = [0] * 10
print(nums3, len(nums3))

nums4 = [None] * 5
print(nums4, len(nums4))