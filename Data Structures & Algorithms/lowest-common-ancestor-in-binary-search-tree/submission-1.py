# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        p <= LCA <= q
        """
        if p.val > q.val:
            p, q = q, p
        cur = root
        while not (p.val <= cur.val <= q.val):
            if cur.val > q.val:
                cur = cur.left
            else:
                cur = cur.right
        return cur