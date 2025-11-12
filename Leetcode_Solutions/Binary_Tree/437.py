from collections import defaultdict

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, target_sum):
        
        def dfs(sum_hash, current_sum, node):
            if not node:
                return 0
            
            # Update the current path sum
            current_sum += node.val
            
            # Calculate the number of valid paths ending at the current node
            path_count = sum_hash[current_sum - target_sum]
            
            # Update the sum_hash with the current path sum
            sum_hash[current_sum] += 1
            
            # Recursively search the left and right subtrees
            path_count += dfs(sum_hash, current_sum, node.left)
            path_count += dfs(sum_hash, current_sum, node.right)
        
            # Backtrack: remove the current path sum from the sum_hash
            sum_hash[current_sum] -= 1
            
            return path_count
        
        # Initialize the sum_hash with the prefix sum of 0 occurring once
        return dfs(defaultdict(int, {0: 1}), 0, root)
        

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
print(Solution().pathSum(root, 8)) # 3

