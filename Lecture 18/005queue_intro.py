from collections import deque


class queue:
    def __init__(self):
        self.d = deque()

    def push(self, val):
        self.d.append(val)

    def pop(self):
        return self.d.popleft()

    def front(self):
        return self.d[0]

    def size(self):
        return len(self.d)

    def empty(self):
        return len(self.d) == 0


q = queue()

q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)

print(q.size())

while not q.empty():
    print(q.pop())

print(q.size())

q = deque()

q.append(10)
q.append(20)
q.append(30)
q.append(40)
q.append(50)

print(len(q))

while len(q) != 0:
    print(q.popleft())

print(len(q))
