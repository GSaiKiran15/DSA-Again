class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, node.val-prev.val)
            prev = node
            dfs(node.right)
        dfs(root)
        return res

