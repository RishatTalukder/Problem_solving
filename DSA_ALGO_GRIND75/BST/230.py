# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         def inorder(node):
#             nonlocal k

#             if not node:
#                 return None
            
#             left = inorder(node.left)
#             if left is not None:
#                 return left
            
#             k -= 1
#             if k == 0:
#                 return node.val
            
#             right = inorder(node.right)
#             if right is not None:
#                 return right
            
#             return None
        
#         return inorder(root)


# recursive way to solve it

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        res = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            if len(res) == k:
                return
            res.append(node.val)
            
            inorder(node.right)

            return

        inorder(root)
        return res[-1]
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        count = 0
        res = None

        def inorder(node):
            nonlocal count, res
            if node is None:
                return None
            inorder(node.left)
            count += 1 
            if count == k:
                res = node.val
                return

            inorder(node.right)

        inorder(root)
        return res
    
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        count = 0
        res = None

        def inorder(node):
            nonlocal count, res
            if not node:
                return None

            inorder(node.left)
            count += 1
            if count == k:
                res = root.val
                return 

            inorder(node.right)

        inorder(root)
        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Test cases
def test_kthSmallest(): 
    solution = Solution()

    # Test case 1
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    result = solution.kthSmallest(root, 1)
    print(f'Test case 1 result: {result}')

    # Test case 2
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    result = solution.kthSmallest(root, 3)
    print(f'Test case 2 result: {result}')
    
    # Test case 3
    root = TreeNode(2)
    root.left = TreeNode(1)
    result = solution.kthSmallest(root, 2)
    print(f'Test case 3 result: {result}')
    assert result == 2

    # Test case 4
    root = TreeNode(1)
    result = solution.kthSmallest(root, 1)
    print(f'Test case 4 result: {result}')
    assert result == 1

test_kthSmallest()