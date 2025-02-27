from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_hamming_distance = 0
        num_count = len(nums)
        
        for bit_position in range(32):
            bit_count = 0
            for num in nums:
                bit_count += (num >> bit_position) & 1
            hamming_distance_at_bit = bit_count * (num_count - bit_count)
            total_hamming_distance += hamming_distance_at_bit
        
        return total_hamming_distance
    
sol = Solution()
print(sol.totalHammingDistance([4,14,2])) # 6