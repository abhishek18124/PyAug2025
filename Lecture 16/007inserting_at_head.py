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


head = None  # init, LinkedList is empty

head = insert_at_head(head, 50)
head = insert_at_head(head, 40)
head = insert_at_head(head, 30)
head = insert_at_head(head, 20)
head = insert_at_head(head, 10)

# if head is None:
#     print("Yes")

print_linked_list(head)  # 10 20 30 40 50

head = delete_at_head(head)

print_linked_list(head)
