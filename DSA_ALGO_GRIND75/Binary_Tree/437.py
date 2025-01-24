from collections import defaultdict

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        
        def dfs(sumHash, prefixSum, node):

            if not node:
                return 0
            
			# Sum of current path
            prefixSum += node.val
            
			# number of paths that ends at current node
            path = sumHash[prefixSum - sum] 
            
			# add currentSum to prefixSum Hash
            sumHash[prefixSum] += 1
            
			# traverse left and right of tree
            path += dfs(sumHash, prefixSum, node.left) + dfs(sumHash, prefixSum, node.right)
        
		    # remove currentSum from prefixSum Hash
            sumHash[prefixSum] -= 1
            
            return path
        
        # depth first search, initialize sumHash with prefix sum of 0, occurring once
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

