# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Good = greatest value on the path

        Traverse dfs with maximum val
        """
        ans = 0
        def dfs(node, cur):
            nonlocal ans

            if not node:
                return 
            
            if node.val >= cur:
                ans += 1
                cur = node.val
            
            dfs(node.left, cur)
            dfs(node.right, cur)


        dfs(root, root.val)
        return ans