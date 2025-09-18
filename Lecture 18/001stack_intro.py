class stack:
    def __init__(self):
        self.l = []

    def push(self, val):
        self.l.append(val)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def size(self):
        return len(self.l)

    def empty(self):
        return len(self.l) == 0


s = stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print(s.size())

while not s.empty():
    print(s.pop())

print(s.size())

# using list to work as a stack directly instead of creating class

s = []

s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)

print(len(s))

while len(s) > 0:
    print(s.pop())

print(len(s))
