class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_linked_list(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


# time : O(n)
# space: O(1)
# [HW] try to reverse the linkedList recursively


def reverse_linked_list(head):
    prev = None
    cur = head
    while cur is not None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev


head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)

print_linked_list(head)

head = reverse_linked_list(head)

print_linked_list(head)
