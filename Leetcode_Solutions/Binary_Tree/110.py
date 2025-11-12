# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def finding_dori(self, root):
        """
        This method recursively checks if a binary tree is balanced or not.
        
        Parameters:
        - root: The root node of the binary tree.
        
        Returns:
        - The height of the binary tree if it is balanced, otherwise -1.
        """
        if root is None:
            return 0

        # Recursively calculate the height of the left and right subtrees
        left = self.finding_dori(root.left)
        right = self.finding_dori(root.right)

        # If either of the subtrees is unbalanced, return -1
        if left == -1 or right == -1:
            return -1

        # If the absolute difference between the heights of the left and right subtrees is greater than 1,
        # return -1 to indicate that the tree is unbalanced
        if abs(left - right) > 1:
            return -1

        # Return the height of the current node by adding 1 to the maximum height of its left and right subtrees
        return 1 + max(left, right)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        This method checks if a binary tree is balanced or not.
        
        Parameters:
        - root: The root node of the binary tree.
        
        Returns:
        - True if the binary tree is balanced, False otherwise.
        """
        # Call the recursive method to check if the binary tree is balanced
        ans = self.finding_dori(root)

        # If the height returned by the recursive method is not -1, it means the tree is balanced
        if ans != -1:
            return True

        # Otherwise, the tree is unbalanced
        return False