# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def dfs(node):
            if not node:
                return 0

            node.val += dfs(node.left) + dfs(node.right)

            return node.val

        total = dfs(root)

        ans = 0

        q = deque([root])


        while q:
            node = q.popleft()

            if not node:
                continue

            curr = (total - node.val)*node.val
            ans = max(ans, curr)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)


        return ans%MOD
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 +7
        def dfs(node):
            if not node:
                return 0

            node.val += dfs(node.right) + dfs(node.left)

            return node.val

        total = dfs(root)

        q = deque([root])
        ans = 0
        while q:
            node = q.popleft()

            cur = (total-node.val)*node.val
            ans = max(ans, cur)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)


        return ans%MOD

