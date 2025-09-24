import heapq


class Solution:
    def connectSticks(self, sticks) -> int:
        heapq.heapify(sticks)

        # at this point of time sticks is transformed into a minHeap

        total = 0

        while len(sticks) > 1:  # n-1 iterations
            a = heapq.heappop(sticks)  # logn
            b = heapq.heappop(sticks)  # logn
            total += a + b  # const
            heapq.heappush(sticks, a + b)  # logn

        return total

        # time : O(nlogn)
        # space: O(n) due to minHeap


s = Solution()
print(s.connectSticks([4, 2, 3, 6]))
