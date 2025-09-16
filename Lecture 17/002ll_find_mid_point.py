class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_linked_list(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


# time : n/2 steps.const ~ O(n)
# space: O(1)


def find_mid_point(head):
    if head is None:
        # LinkedList is empty
        return None

    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


head = None
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)
head.next.next.next.next.next = ListNode(60)

print_linked_list(head)

mid_point = find_mid_point(head)
if mid_point is not None:
    print(mid_point.val)
else:
    print("LinkedList is empty")
