class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# time : O(n)
# space: O(hgt of the tree) due to fn call stack


def dfs(root) -> int:
    # base case
    if root is None:
        # tree is empty
        return 0

    # recursive case

    # f(root) = find the sum of nodes in the given tree

    # 1. ask your friend to find the sum of nodes in the left_sub_tree

    x = dfs(root.left)

    # 2. ask your friend to find the sum of nodes in the right_sub_tree

    y = dfs(root.right)

    return x + y + root.val


root = None  # init tree is empty
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(60)
root.left.right.left = TreeNode(70)

print(dfs(root))
