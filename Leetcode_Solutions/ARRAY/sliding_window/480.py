from bisect import insort


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = []
        window = sorted(nums[:k])
        is_odd = k % 2
        for i in range(k, len(nums)+1):
            if is_odd:
                median.append(window[k//2])
            else:
                median.append((window[k//2-1] + window[k//2]) / 2)
            
            if i == len(nums):
                break
            
            window.pop(bisect_left(window, nums[i-k]))
            insort(window, nums[i])

        return median