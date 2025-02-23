class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root
        
        # Find left subtree root (second element in preorder)
        left_root = preorder[1]

        # Find index of left_root in postorder to determine the boundary
        left_subtree_size = postorder.index(left_root) + 1

        # Correctly partition preorder and postorder
        left_preorder = preorder[1:left_subtree_size + 1]
        right_preorder = preorder[left_subtree_size + 1:]

        left_postorder = postorder[:left_subtree_size]
        right_postorder = postorder[left_subtree_size:-1]

        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)

        return root
