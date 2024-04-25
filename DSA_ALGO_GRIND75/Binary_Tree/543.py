# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the diameter of a binary tree.

        The diameter of a binary tree is defined as the length of the longest path between any two nodes in the tree.
        The path may or may not pass through the root.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            int: The diameter of the binary tree.

        """

        max_d = 0

        def dfs(root):
            """
            Depth-first search to calculate the height of each node and update the maximum diameter.

            Args:
                root (TreeNode): The current node in the depth-first search.

            Returns:
                int: The height of the current node.

            """

            nonlocal max_d

            if not root:
                return -1

            # Recursively calculate the height of the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # Update the maximum diameter if necessary
            max_d = max(max_d, left + right + 2)

            # Return the height of the current node
            return 1 + max(left, right)

        # Start the depth-first search from the root node
        dfs(root)

        # Return the maximum diameter of the binary tree
        return max_d
