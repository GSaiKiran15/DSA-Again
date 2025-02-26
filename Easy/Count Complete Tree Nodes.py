class Solution:
    def countNodes(self, root) -> int:
        if root is None: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        if root is None:
            return 0
        res = 0
        queue = [root]
        while queue:
            root = queue.pop(0)
            res += 1
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return res

