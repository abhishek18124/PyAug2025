def is_prime(n: int)->bool:
	i = 2
	while i*i <= n:
		if n%i == 0:
			# you've found a factor of n in range 2 to root n
			return False
		i += 1
	return True # you did not find any factor of n in the 2 to root so it is prime


def print_primes(m:int)->None:
	for n in range(2, m+1): # [2, m+1) # [2, m]
		# check if n is a prime no. or not
		if is_prime(n):
			print(n)

m = int(input())
print_primes(m)