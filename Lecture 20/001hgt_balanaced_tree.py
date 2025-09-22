class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def hgt(root):
    # base case

    if root is None:
        # tree is empty
        return -1

    # recursive case

    # f(root) = find the height of the given tree

    # 1. ask your friend to find the height of the left_sub_tree

    hgt_left = hgt(root.left)

    # 2. ask your friend to find the height of the right_sub_tree

    hgt_right = hgt(root.right)

    return 1 + max(hgt_left, hgt_right)


# time : O(n^2) worst case when tree is skewed
# time : O(nlogn) when tree is balanced

# space: O(h) due to function call stack


def dfs(root) -> bool:
    # base case
    if root is None:
        return True  # empty is hgt_balanced

    # recursive case

    # f(root) = check if the given tree is height balanced or not

    # 1. ask your friend to check if the left_subtree is height balanced or not

    left_is_bal = dfs(root.left)

    # 2. ask your friend to check if the right_subtree is height balanced or not

    right_is_bal = dfs(root.right)

    # 3. check if the height balance property works at the root or not

    root_is_bal = True if abs(hgt(root.left) - hgt(root.right)) <= 1 else False

    return left_is_bal and right_is_bal and root_is_bal


root = None
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(60)
root.left.right.left = TreeNode(70)

print(dfs(root))
