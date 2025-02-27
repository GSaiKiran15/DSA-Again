class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
tree = BinaryTree(5, BinaryTree(4, BinaryTree(11, BinaryTree(7), BinaryTree(2))), BinaryTree(8, BinaryTree(13), BinaryTree(4, None, BinaryTree(1))))

def sol(root):
    if not root:
        return 0
    stack = [root]
    output = [100000,100000]
    while stack:
        root = stack.pop(-1)
        if root.val < output[0]:
            output[1] = output[0]
            output[0] = root.val
            
        elif root.val < output[1]:
            output[1] = root.val
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return output[1] - output[0]
    # def dfs(node, curSum):
    #     if not root:
    #         return False

    #     curSum += root.val
    #     if not root.left and not root.right:
    #         return curSum == targetSum
        
    #     return ((dfs(root.left)) or (dfs(root.right)))

sol(tree)
         