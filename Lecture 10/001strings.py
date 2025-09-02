s = "coding"
print(s)
print(len(s))

# we can index into a string obj
print(s[0])
print(s[1])
print(s[2])
print(s[-1])
print(s[-2])

# we can create slices of a string obj

print(s[1:4])

# iterating over a string obj

for ch in s:
	print(ch, end=' ')
print()

for i, ch in enumerate(s):
	print(i, ch)

# string obj is immutable

# s[0] = 'x' # TypeError since str obj doesn't support item assignment

# concatenating string objects

s1 = "coding"
s2 = "blocks"

s3 = s1+s2
print(s3)

s1 = "HELLO"
s1 = s1.lower()
print(s1)

s2 = "world"
s2 = s2.upper()
print(s2)

s = "    hello world     "
print(s)
s = s.strip() # s.lstrip() # s.rstrip()
print(s)

s = "the sun rises in the east, they sun sets in the west"
print(s.find("sun"))
print(s.rfind("sun"))
print(s.find("moon"))
print(s.rfind("moon"))

s = "hi how   are   you ?"
print(s.split())
l = s.split()
print(type(l))
for word in l:
	print(word)

sports = "badminton,cricket,football,tennis"
print(sports.split(','))

fruits = "apple, orange, banana, kiwi"
print(fruits.split(', '))

nums = ["10", "20", "30", "40"]
s = "-".join(nums)
print(s, type(s))

# string interpolation

country = "India"
year = 1947

print(f"{country} gained its independence from British in {year}")

