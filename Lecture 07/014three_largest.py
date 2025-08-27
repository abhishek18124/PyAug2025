import sys

nums = [20, 5, 0, 25, 15, 10]

first_max_so_far = -sys.maxsize-1
second_max_so_far = -sys.maxsize-1
third_max_so_far = -sys.maxsize-1

# time : O(n) assuming nums has n elements

for cur in nums:
	if cur > first_max_so_far:
		third_max_so_far = second_max_so_far
		second_max_so_far = first_max_so_far
		first_max_so_far = cur
	elif cur > second_max_so_far:
		third_max_so_far = second_max_so_far
		second_max_so_far = cur
	elif cur > third_max_so_far:
		third_max_so_far = cur

print(first_max_so_far, second_max_so_far, third_max_so_far)