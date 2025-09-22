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
    while len(q) > 0:
        cur = q.popleft()
        # process cur node
        print(cur.val, end=" ")
        if cur.left is not None:
            # visit the left child of the cur node
            q.append(cur.left)
        if cur.right is not None:
            # visit the right child of the cur node
            q.append(cur.right)
    print()


root = None
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(60)
root.left.right.left = TreeNode(70)

bfs(root)
