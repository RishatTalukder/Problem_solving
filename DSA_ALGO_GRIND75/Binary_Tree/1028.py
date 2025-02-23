# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.idx = 0

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        return self.dfs(traversal, 0)   

    def dfs(self, traversal, depth):
        if self.idx == len(traversal):
            return None

        level = 0
        while self.idx + level < len(traversal) and traversal[self.idx + level] == '-':
            level += 1

        if level != depth:
            return None

        self.idx += level
        start = self.idx
        while self.idx < len(traversal) and traversal[self.idx] != '-':
            self.idx += 1

        node = TreeNode(int(traversal[start:self.idx]))
        node.left = self.dfs(traversal, depth + 1)
        node.right = self.dfs(traversal, depth + 1)

        return node        