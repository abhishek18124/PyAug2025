import heapq

l = []  # internal representation of minHeap

heapq.heappush(l, (2, 3))
heapq.heappush(l, (3, 4))
heapq.heappush(l, (1, 2))
heapq.heappush(l, (1, 1))
heapq.heappush(l, (5, 5))
heapq.heappush(l, (2, 0))

print(l)

# by default minHeap prop. is based on the 1st value of the tuple
# if the 1st element of the tuples match then minHeap prop. is based on next value of the tuple

while l:
    print(heapq.heappop(l))
