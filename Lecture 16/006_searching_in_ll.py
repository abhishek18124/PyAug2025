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


def search_linked_list(head, target):
    while head is not None:
        if head.val == target:  # target found
            return True
        head = head.next

    return False  # target not found


# time : O(n)
# space: O(n) due to function call stack


def search_linked_list_recursive(head, target):
    # base case
    if head is None:
        return False

    # recursive case
    if head.val == target:
        return True
    else:
        # ask your friend to search for the target in the
        # sublist that starts from the node which comes
        # after the head node
        return search_linked_list_recursive(head.next, target)


head = None  # LinkedList is empty

head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)

print_linked_list(head)

target = 30

print(search_linked_list(head, target))

print(search_linked_list_recursive(head, target))

target = 100

print(search_linked_list(head, target))

print(search_linked_list_recursive(head, target))
