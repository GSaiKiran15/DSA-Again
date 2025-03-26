def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def pot(node, output):
            if not node:
                return
            output.append(node.val)
            pot(node.left, output)
            pot(node.right, output)
        pot(root, output)
        return output
