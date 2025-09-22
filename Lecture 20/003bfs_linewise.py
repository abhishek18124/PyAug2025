from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# time : O(n)
# space: O(n) due to queue


def bfs(root) -> None:
    if root is None:
        return

    q = deque()
    q.append(root)
    q.append(None)

    while len(q) > 0:
        cur = q.popleft()
        if cur is None:
            print()
            if len(q) > 0:
                q.append(None)
        else:
            # process cur node
            print(cur.val, end=" ")
            if cur.left is not None:
                # visit the left child of the cur node
                q.append(cur.left)
            if cur.right is not None:
                # visit the right child of the cur node
                q.append(cur.right)
    print()


def build_tree():
    val = int(input())
    root = TreeNode(val)

    q = deque()
    q.append(root)

    while len(q) > 0:
        cur = q.popleft()

        # build the left and right child for cur node

        val = int(input())
        if val != -1:
            cur.left = TreeNode(val)
            q.append(cur.left)

        val = int(input())
        if val != -1:
            cur.right = TreeNode(val)
            q.append(cur.right)

    return root


root = build_tree()

bfs(root)
