class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_linked_list(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


head = None  # LinkedList is empty

head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)

print_linked_list(head)
