import sys

n = int(input())
max_so_far = -sys.maxsize - 1

for _ in range(n): # conventially _ is used as var name when we are not using the var
	x = int(input())
	if x > max_so_far:
		max_so_far = x

print(max_so_far)