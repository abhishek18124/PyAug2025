class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# time : O(n)
# space: O(hgt of tree) due to fn call stack


def dfs(root):
    # base case

    if root is None:
        # tree is empty
        return -1

    # recursive case

    # f(root) = find the height of the given tree

    # 1. ask your friend to find the height of the left_sub_tree

    hgt_left = dfs(root.left)

    # 2. ask your friend to find the height of the right_sub_tree

    hgt_right = dfs(root.right)

    return 1 + max(hgt_left, hgt_right)


root = None  # init tree is empty
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(60)
root.left.right.left = TreeNode(70)

print(dfs(root))
