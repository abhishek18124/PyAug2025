from collections import Counter # import just Counter from the collections module

# import collections # import the entire collections module

s = "state"
t = "taste"

print(Counter(s))
print(Counter(t))

print(Counter(s) == Counter(t))

