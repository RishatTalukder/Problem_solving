# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        parent = {root:None}

        q = deque([root])

        last_level = []

        while q:
            n = len(q)
            last_level = []

            for _ in range(n):
                node = q.popleft()
                last_level.append(node)

                if node.left:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right:
                    parent[node.right] = node
                    q.append(node.right)


        deepest = set(last_level)

        while len(deepest)> 1:
            deepest = {parent[node] for node in deepest}


        return deepest.pop()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        parents = {root:None}

        q = deque([root])

        last = []

        while q:
            last = []
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                last.append(node)

                if node.left:
                    q.append(node.left)
                    parents[node.left] = node

                if node.right:
                    q.append(node.right)
                    parents[node.right] = node


        deep = set(last)

        while len(deep)>1:
            deep = {parents[node] for node in deep}


        return deep.pop()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        parents = {root:None}

        q = deque([root])
        last = []
        while q:
            last = []
            n = len(q)

            for i in  range(n):
                node = q.popleft()
                last.append(node)

                if node.left:
                    parents[node.left] = node
                    q.append(node.left)

                if node.right:
                    parents[node.right] = node
                    q.append(node.right)


        deep = set(last)

        while len(deep) > 1:
            deep = {parents[node] for node in deep}

        return deep.pop()
