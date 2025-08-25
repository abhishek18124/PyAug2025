n = int(input())

i = 2
while i <= int(n ** 0.5):
	if n%i == 0:
		print(n, "is not prime no.")
		break
	i = i + 1

if i > int(n ** 0.5):
	print(n, "is prime no.")

