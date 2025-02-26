class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def average(root):
    if root is None:
        return []
    res = []
    queue = [root]
    while queue:
        level_length = len(queue)
        level_sum = 0
        
        for _ in range(level_length):
            root = queue.pop(0)
            level_sum += root.val
            if queue.left:
                queue.append(root.left)
            if queue.right:
                queue.append(root.right)
        res.append(level_sum / level_length)
    return res


        