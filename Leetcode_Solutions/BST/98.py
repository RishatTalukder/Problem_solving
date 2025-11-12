# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is a valid binary search tree.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            bool: True if the binary tree is a valid binary search tree, False otherwise.
        """
        
        def validity(node, lower, upper):
            # Base case: if node is None, it is a valid BST
            if node is None:
                return True
            
            val = node.val
            # Check if the current node's value is within the valid range
            if val <= lower or val >= upper:
                return False
            
            # Recursively check the left and right subtrees
            if not validity(node.left, lower, val):
                return False
            
            if not validity(node.right, val, upper):
                return False
            
            return True
        
        # Start the recursive validity check from the root node
        return validity(root, float('-inf'), float('inf'))
