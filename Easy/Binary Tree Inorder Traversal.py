class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def iot(node):
            if not node:
                return 
            iot(node.left)
            res.append(node.val)
            iot(node.right)
        iot(root)
        return res