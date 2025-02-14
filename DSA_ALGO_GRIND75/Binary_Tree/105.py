from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def builder(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            root = preorder,popleft()
            node = TreeNode(root)
            index = inorder.index(root)

            node.left = builder(preorder, inorder[:index])
            node.right = builder(preorder, inorder[index + 1:])


            return node
        
        return builder(deque(preorder), inorder)