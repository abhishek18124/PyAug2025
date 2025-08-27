nums = [1, 2, 3, 4, 5]
squares = [num**2 for num in nums]
print(squares)

# n = int(input())
# arr = []
# for _ in range(n):
# 	arr.append(int(input()))
# print(arr, len(arr))

n = int(input())
arr = [int(input()) for _ in range(n)]
print(arr, len(arr))

nums = [1, 2, 3, 4, 5, 6]
even_nums = [num for num in nums if num%2 == 0]
print(even_nums, len(even_nums))