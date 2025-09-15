class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_linked_list(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


# time : O(1)


def insert_at_head(head, val):
    n = ListNode(val)
    n.next = head
    head = n
    return head


# time : O(1)


def delete_at_head(head):
    if head is None:
        return None

    head = head.next
    return head


def get_tail(head):
    while head.next is not None:
        head = head.next
    return head


# time : O(n)
# space: O(1)
def insert_at_tail(head, val):
    if head is None:
        head = insert_at_head(head, val)
        return head

    n = ListNode(val)  # const
    tail = get_tail(head)  # linear
    tail.next = n  # const

    return head


# time : O(n)
# space: O(1)
def delete_at_tail(head):
    if head is None:
        # LinkedList is empty
        return None

    if head.next is None:
        # LinkedList has one node
        head = delete_at_head(head)
        return head

    prev = None
    cur = head

    while cur.next is not None:
        prev = cur
        cur = cur.next

    # cur is pointing to tail node
    # and prev is one step behind cur

    prev.next = None
    return head


head = None  # init, LinkedList is empty

head = insert_at_head(head, 50)
head = insert_at_head(head, 40)
head = insert_at_head(head, 30)
head = insert_at_head(head, 20)
head = insert_at_head(head, 10)

print_linked_list(head)  # 10 20 30 40 50

head = insert_at_tail(head, 60)

print_linked_list(head)

head = delete_at_tail(head)

print_linked_list(head)
