n = int(input())
ans = 0

while ans*ans <= n:
	ans = ans + 1

ans = ans - 1

while ans*ans <= n:
	ans = ans + 0.1

ans = ans - 0.1

while ans*ans <= n:
	ans = ans + 0.01

ans = ans - 0.01

while ans*ans <= n:
	ans = ans + 0.001

ans = ans - 0.001

print(ans)

# [HW] generalise this program for any precision p

# input : n = 2 p = 3
# output : 1.414

# input : n = 3 p = 2
# output : 1.73
