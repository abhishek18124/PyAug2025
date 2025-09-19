class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


s = 0  # to track sum of tree nodes

# time : O(n)
# space: O(hgt of the tree) due to fn call stack


def dfs(root):
    # base case
    if root is None:
        return

    # recursive case

    global s

    s += root.val
    dfs(root.left)
    dfs(root.right)


root = None  # init tree is empty
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(60)
root.left.right.left = TreeNode(70)

dfs(root)

print(s)
