class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        if not subRoot:
            return True

        if not root:
            return False

        # Try matching starting at current node
        if sameTree(root, subRoot):
            return True

        # Otherwise search elsewhere in root
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )