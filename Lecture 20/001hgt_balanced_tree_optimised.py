class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# time : O(n)
# space: O(h) due to function call stack


def dfs(root) -> tuple[int]:
    # base case
    if root is None:
        return -1, True  # empty tree has a hgt of -1, empty is hgt_balanced

    # recursive case

    # f(root) = check if the given tree is height balanced or not

    # 1. ask your friend to check if the left_subtree is height balanced or not

    left_hgt, left_is_bal = dfs(root.left)

    # 2. ask your friend to check if the right_subtree is height balanced or not

    right_hgt, right_is_bal = dfs(root.right)

    # 3. check if the height balance property works at the root or not

    root_is_bal = True if abs(left_hgt - right_hgt) <= 1 else False

    return 1 + max(left_hgt, right_hgt), left_is_bal and right_is_bal and root_is_bal


root = None
root = TreeNode(10)
root.left = TreeNode(20)
root.left.left = TreeNode(30)


hgt, is_bal = dfs(root)
# print(hgt)
print(is_bal)
