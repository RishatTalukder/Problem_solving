class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        summ = 0

        while queue:
            node = queue.popleft()
            if node.left:
                if not node.left.left and not node.left.right:
                    summ += node.left.val
                else:
                    queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return summ

class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0
        
        def dfs(node,isleft):
            if not node:
                return 0
            if not node.left and not node.right and isleft:
                return node.val
            
            return dfs(node.left,True) + dfs(node.right,False)
        
        return dfs(root,False)
    
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0
        
        queue = deque()
        
        if root.left:
            queue.append(root.left)
        
        if root.right:
            queue.append(root.right)

        summ = 0

        while queue:
            summ += queue[0].val

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return summ






sol = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sol.sumOfLeftLeaves(root)) # 24


