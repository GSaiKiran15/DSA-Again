class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def dfs(tree):
    stack = [tree]
    while stack:
        root = stack.pop()
        print(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        
def dfs_recursive(node):
    if not node:
        return
    print(node.val)
    dfs_recursive(node.left)
    dfs_recursive(node.right)

tree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))
dfs(tree)
dfs_recursive(tree)