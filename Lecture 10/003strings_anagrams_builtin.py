# from collections import Counter

import collections

s = "state"
t = "taste"

print(collections.Counter(s))
print(collections.Counter(t))

print(collections.Counter(s) == collections.Counter(t))

