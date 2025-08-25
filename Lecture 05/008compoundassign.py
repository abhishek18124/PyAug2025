a = 10
b = 5
a += b * 3
print(a)


# a op= b
# a = a op b

# a = a + (b * 3)
# a = 10 + 5 * 3
# a = 10 + 15
# a = 25

x = 7
y = 4
x *= y - 2
print(x)

# x *= y - 2
# wrong expansion
# x = x * y - 2
# x = 7 * 4 - 2
# x = 28 - 2
# x = 26
# right expansion
# x *= y - 2
# x = x * (y-2)
# x = 7 * (4-2)
# x = 7 * 2
# x = 14 