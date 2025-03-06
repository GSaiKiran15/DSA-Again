# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        output = [root.val]
        children = []
        while queue:
            for i in queue:
                if i.left:
                    children.append(i.left)
                if i.right:
                    children.append(i.right)
            if not children:
                return output
            output.append(children[-1].val)
            queue = children
            children = []
        return output
