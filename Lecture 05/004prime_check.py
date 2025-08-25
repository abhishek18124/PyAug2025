n = int(input())

i = 2
flag = True # assuming n is a prime no.
while i <= int(n ** 0.5):
	if n%i == 0:
		print(n, "is not prime no.")
		flag = False # our assumption was wrong
		break
	i = i + 1

if flag:
	print(n, "is prime no.")

