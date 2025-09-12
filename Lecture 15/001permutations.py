def f(inp:list[str], i:int)->None:
	# base case
	if i == len(inp):
		print("".join(inp))
		return

	# recursive case

	# f(i) = it is fn that takes decisions for position i to n-1

	# decide for the ith position

	for j in range(i, len(inp)):
		inp[i], inp[j] = inp[j], inp[i]
		f(inp, i+1)
		inp[i], inp[j] = inp[j], inp[i] # backtracking


s = "abc"
inp = list(s)
f(inp, 0)