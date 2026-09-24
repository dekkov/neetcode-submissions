# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        POS, NEG = float('inf'), -1*float('inf')
        def dfs(node, minL, maxL):
            
            if not node:
                return True

            if not (minL < node.val < maxL):
                return False

            return dfs(node.left, minL, node.val) and dfs(node.right, node.val, maxL)

        
        return dfs(root, NEG, POS)

        
