# def is_prime(n: int)->bool:
# 	i = 2
# 	while i <= int(n**0.5):
# 		if n%i == 0:
# 			# you've found a factor of n in range 2 to root n
# 			return False
# 		i += 1
# 	return True # you did not find any factor of n in the 2 to root so it is prime

def is_prime(n: int)->bool:
	i = 2
	while i*i <= n:
		if n%i == 0:
			# you've found a factor of n in range 2 to root n
			return False
		i += 1
	return True # you did not find any factor of n in the 2 to root so it is prime



print(is_prime(7)) # True
print(is_prime(4)) # False