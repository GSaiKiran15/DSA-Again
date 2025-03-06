# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        child = []
        values = []
        output = [[root.val]]
        while queue:
            for i in queue:
                if i.left:
                    child.append(i.left)
                    values.append(i.left.val)
                if i.right:
                    child.append(i.right)
                    values.append(i.right.val)
            if not child:
                return output
            output.append(values)
            queue = child
            child = []
            values = []

        return output