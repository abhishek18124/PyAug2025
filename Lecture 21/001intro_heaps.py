import heapq

l = []  # l is the internal representation of heap

heapq.heappush(l, 3)
heapq.heappush(l, 2)
heapq.heappush(l, 5)
heapq.heappush(l, 4)
heapq.heappush(l, 1)

print(l)

# while len(l) > 0:
#     print(heapq.heappop(l))

while l:
    print(heapq.heappop(l))

# while len(l) > 0:
#     print(l[0])
#     heapq.heappop(l)
