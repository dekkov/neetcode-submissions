# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), self.findLongest(root.left) + self.findLongest(root.right))
        
    def findLongest(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.findLongest(root.left), self.findLongest(root.right))