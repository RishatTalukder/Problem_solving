#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        def dfs(index, current, total):
            if index >= len(candidates) or total > target:
                return
            
            if total == target:
                res.append(current.copy())
                return
            
            current.append(candidates[index])
            dfs(index, current, total+candidates[index])

            current.pop()
            dfs(index+1, current, total)
        
        dfs(0,[],0)

        return res
        
# @lc code=end

