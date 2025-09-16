class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_linked_list(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


def remove_cycle(head):
    # 1. find the meeting point

    slow = head
    fast = head

    while True:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    # slow & fast are at the meeting point

    # 2. move temp one-step behind the meeting point

    temp = head
    while temp.next is not fast:
        temp = temp.next

    # temo is now one-step behind the meeting

    # 3. take slow to head and move slow, temp, fast
    # at the same speed till slow and fast meet again

    slow = head
    while slow is not fast:
        temp = temp.next
        slow = slow.next
        fast = fast.next

    # at this point slow and fast are at the start of
    # the cycle and therefore temp is the tail of the
    # linkedList

    temp.next = None


head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)
head.next.next.next.next.next = ListNode(60)
head.next.next.next.next.next.next = head.next.next

remove_cycle(head)

print_linked_list(head)  # 10 20 30 40 50 60
