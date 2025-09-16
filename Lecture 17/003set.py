s = {1, 2, 3, 4, 5}
print(type(s))
print(len(s))
print(s)
s.add(6)
print(s)
s.remove(3)
print(s)
s.add(1)  # nothing will happen as 1 is already present
print(s)
# s.remove(10) # KeyError since 10 doesn't exist in the set
s.discard(5)
print(s)
s.discard(10)  # no KeyError
print(2 in s)
print(10 in s)

for item in s:
    print(item)


st = "hello"
s = set(st)
print(s)

ls = [10, 20, 30, 10, 20]
s = set(ls)
print(s)

em = set()
print(em)
print(type(em))
print(len(em))
