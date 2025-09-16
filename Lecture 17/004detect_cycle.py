class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# time : on avg. O(n)
# space: O(n) due set


class Solution:
    def hasCycle(self, head) -> bool:
        s = set()
        while head is not None:
            if head in s:
                return True
            s.add(head)
            head = head.next

        return False  # no cycle found


head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)
head.next.next.next.next.next = ListNode(60)
head.next.next.next.next.next.next = head.next.next

soln = Solution()
print(soln.hasCycle(head))
