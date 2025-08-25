n = 42
k = 4
mask = 1 << k
print(n | mask) # set the kth bit of n

n = 42
k = 3
mask = ~(1 << k)
print(n & mask) # clear the kth bit of n

n = 42
k = 3

print((n>>k)&1)

n = 42
k = 4

print((n>>k)&1)
