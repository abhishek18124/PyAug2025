class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_pre_order(root):
    # base case
    if root is None:
        print(-1, end=" ")
        return

    # recursive case

    # f(root) = print the pre_order of the given tree

    # 1. process the root node
    print(root.val, end=" ")

    # 2. ask your friend to print the pre_order of the left_subtree
    print_pre_order(root.left)

    # 3. ask your friend to print the pre_order of the right_subtree
    print_pre_order(root.right)


def print_in_order(root):
    # base case
    if root is None:
        print(-1, end=" ")
        return

    # recursive case

    # f(root) = print the in_order of the given tree

    # 1. ask your friend to print the in_order of the left_subtree
    print_in_order(root.left)

    # 2. process the root node
    print(root.val, end=" ")

    # 3. ask your friend to print the in_order of the right_subtree
    print_in_order(root.right)


root = None  # init tree is empty
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(60)
root.left.right.left = TreeNode(70)

print_pre_order(root)
print()
print_in_order(root)
