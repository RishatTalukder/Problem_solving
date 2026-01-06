# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        maxx = root.val
        level = 1
        ans = level

        while q:
            new_q = deque()
            sm = 0
            for node in q:
                
                if node.left:
                    new_q.append(node.left)
                    sm += node.left.val

                if node.right:
                    new_q.append(node.right)
                    sm += node.right.val

            q = new_q
            level += 1
            if sm > maxx and q:
                ans = level
                maxx = sm

        return ans
            

            