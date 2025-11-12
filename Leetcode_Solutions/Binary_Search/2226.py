class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_candies_in_a_pile = max(candies)
        n = len(candies)
        left = 0
        right = max_candies_in_a_pile

        def can_allocate_candies(candies: List[int], k: int, mid: int) -> bool:
            mx_num_children = 0
            for candy in candies:
                mx_num_children += candy // mid
            return mx_num_children >= k
        
        while left < right:
            mid = (left + right + 1) // 2
            if can_allocate_candies(candies, k, mid):
                left = mid
            else:
                right = mid - 1

        return left