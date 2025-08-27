n = int(input())
nums = [int(input()) for _ in range(n)]
print(nums)
# copy_reversed = list(reversed(nums))
# print(copy_reversed)
copy_reversed = nums[::-1]
print(copy_reversed)
print(nums)



lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[1:6]) # start:end:step
print(lst[1:6:2])
print(lst[::-1])