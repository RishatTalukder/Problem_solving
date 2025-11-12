class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search algorithm using recursion
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binary_search(mid + 1, right)
                else:
                    return binary_search(left, mid - 1)
            else:
                return -1
            
        return binary_search(0, len(nums) - 1)