def f(n:int, src:str, hlp:str, dst:str)->None:
	# base case

	if n == 0:
		return

	# recursive case

	# move n disks from src to dst using hlp

	# 1. ask your friend to move n-1 disks from src to hlp using dst

	f(n-1, src, dst, hlp)

	# 2. move the largest disk from src to dst

	print(f"move disk from {src} to {dst}")

	# 3. ask your friend to move n-1 disks from hlp to dst using src

	f(n-1, hlp, src, dst)

n = int(input())
f(n, 'A', 'B', 'C')