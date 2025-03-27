class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        def dfs(node, su):

        

# Example usage:
if __name__ == "__main__":
    # Construct the binary tree:
    #      1
    #     / \
    #    2   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    sol = Solution()
    # You will replace the next line with your own logic
    result = sol.sumNumbers(root)
    print("Sum of root-to-leaf numbers:", result)
