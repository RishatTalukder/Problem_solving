from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count2 = Counter(nums2)  # Tracks frequencies of nums2 elements

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val

        # Update Counter
        self.count2[old_val] -= 1
        if self.count2[old_val] == 0:
            del self.count2[old_val]
        self.count2[new_val] += 1

        # Update the actual value
        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        result = 0
        for num in self.nums1:
            complement = tot - num
            result += self.count2.get(complement, 0)
        return result
