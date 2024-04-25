class Solution:
    """
    This class represents a solution to the problem of finding the maximum depth of a binary tree.

    The maximum depth of a binary tree is defined as the number of nodes along the longest path from the root node
    down to the farthest leaf node.

    Attributes:
        None

    Methods:
        maxDepth: Calculates the maximum depth of a binary tree.

    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum depth of a binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The maximum depth of the binary tree.

        """

        max_d = 0

        def dfs(root):
            nonlocal max_d

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            max_d = 1 + max(left, right)

            return max_d

        dfs(root)

        return max_d
