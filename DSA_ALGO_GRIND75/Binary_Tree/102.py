# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, return the level order traversal of its nodes' values.
        (i.e., from left to right, level by level).

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[List[int]]: The level order traversal of the binary tree.

        Example:
            Given the following binary tree:

                3
               / \
              9  20
                /  \
               15   7

            The level order traversal of the binary tree would be:
            [
                [3],
                [9, 20],
                [15, 7]
            ]

        """

        if not root:
            return []
        
        queue = deque([root])

        res = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                lavel.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res