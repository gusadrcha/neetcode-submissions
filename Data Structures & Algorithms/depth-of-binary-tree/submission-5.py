# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        
        def dfs(root, currDepth):
            if not root:
                return 0

            currDepth += 1
            
            left = dfs(root.left, currDepth)
            right = dfs(root.right,currDepth)

            self.maxDepth = max(self.maxDepth, currDepth)

            return currDepth
        
        dfs(root, 0)

        return self.maxDepth