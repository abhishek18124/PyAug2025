colors = ["red", "green", "blue", "white"]
print(len(colors))
for c in colors:
	print(c, end=' ')
print()

colors[1:3] = ["pink", "orange"]
for c in colors:
	print(c, end=' ')
print()

colors[1:3] = ["magenta", "yellow", "mustard"]
for c in colors:
	print(c, end=' ')
print()
print(len(colors))

colors[1:3] = ["black"]
for c in colors:
	print(c, end=' ')
print()
