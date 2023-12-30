
class Solution:
    def combinationSum(self, candidates, target):
        # create a result list
        result = []

        # create a dfs function that takes index, current and total as arguments
        def dfs(index, current, total):
            # check if the total is equal to the target or not
            if total == target:
                result.append(current.copy())
                return
            # check if the total is greater than the target or not
            if total > target or index >= len(candidates):
                return
            
            current.append(candidates[index]) # append the current item to the current list

            dfs(index, current, total+candidates[index]) # call the dfs function with index, current and total+candidates[index] as arguments

            current.pop() # remove the last item from the current list

            dfs(index+1, current, total) # call the dfs function with index+1, current and total as arguments

        dfs(0, [], 0) # call the dfs function with 0, [], 0 as arguments

        return result