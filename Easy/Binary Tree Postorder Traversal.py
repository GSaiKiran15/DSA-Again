class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def pot(node):
            if not node:
                return
            pot(node.left)
            pot(node.right)
            res.append(node.val)
        pot(root)
        return res