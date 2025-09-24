import heapq

l = [3, 2, 4, 5, 1]

heapq.heapify(
    l
)  # transforms l into a minHeap in-place # more efficient than iterating over l and pushing each value in the heap

print(l)

while l:
    print(heapq.heappop(l))
