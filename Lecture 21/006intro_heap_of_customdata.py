import heapq


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f"{self.name} {self.age}"


l = [Customer("Aryabhata", 74), Customer("Ramanujan", 34), Customer("Homi", 53)]
heapq.heapify(l)

while l:
    print(heapq.heappop(l))
