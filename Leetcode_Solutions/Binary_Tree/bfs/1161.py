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
            


from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        current_level = 1
        max_sum = root.val
        max_sum_level = 1

        while queue:
            next_queue = deque()
            level_sum = 0

            for node in queue:
                if node.left:
                    level_sum += node.left.val
                    next_queue.append(node.left)

                if node.right:
                    level_sum += node.right.val
                    next_queue.append(node.right)

            current_level += 1

            if next_queue and level_sum > max_sum:
                max_sum = level_sum
                max_sum_level = current_level

            queue = next_queue

        return max_sum_level
