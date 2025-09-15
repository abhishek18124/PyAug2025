class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


l1 = ListNode(10)
l2 = ListNode(20)

l1.next = l2

l3 = ListNode(30)
l2.next = l3

l4 = ListNode(40)
l3.next = l4

l5 = ListNode(50)
l4.next = l5
