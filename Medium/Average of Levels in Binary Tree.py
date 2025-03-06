# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        
        queue = [root]
        output = []
        
        while queue:
            level_length = len(queue)
            level_sum = 0
            
            for _ in range(level_length):
                node = queue.pop(0)
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Calculate the average for the current level
            output.append(level_sum / level_length)
        
        return output