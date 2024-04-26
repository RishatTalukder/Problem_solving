# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor of two nodes in a binary tree.

        Args:
            root (TreeNode): The root node of the binary tree.
            p (TreeNode): The first node.
            q (TreeNode): The second node.

        Returns:
            TreeNode: The lowest common ancestor of p and q.

        Steps:
        1. If the root is None or either p or q is equal to the root, return the root.
        2. Recursively find the lowest common ancestor in the left and right subtrees.
        3. If both the left and right subtrees have a valid lowest common ancestor, return the root.
        4. Otherwise, return the valid lowest common ancestor from either the left or right subtree.

        """
        # If root is None or either p or q is equal to root, return root
        if not root or p == root or q == root:
            return root 
        
        # Recursively find the lowest common ancestor in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees have a valid lowest common ancestor, return root
        if left and right:
            return root 
        
        # Otherwise, return the valid lowest common ancestor from either left or right subtree
        return left or right