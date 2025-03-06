class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = None
        if arr[i] is not None:  # Only non-null values are inserted
            temp = TreeNode(arr[i])
            root = temp  # Insert current node

            # insert left child
            root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)

            # insert right child
            root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
        return root

def buildTree(lst):
    n = len(lst)
    root = None
    root = insertLevelOrder(lst, root, 0, n)
    return root

# Example usage:
lst = [3,9,20,None,None,15,7]  # Input list to be converted into a binary tree
root = buildTree(lst)  # root will be the root of the binary tree
