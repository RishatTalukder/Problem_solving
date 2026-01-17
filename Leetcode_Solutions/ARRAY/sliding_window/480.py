from bisect import insort, bisect_left


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
    
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        med = []
        window = sorted(nums[:k])
        is_odd = k%2

        for i in range(k, len(nums)+1):
            if is_odd:
                med.append(window[k//2])

            else:
                median = (window[k//2-1] + window[k//2])/2
                med.append(median)

            if i == len(nums):
                break

            window.pop(bisect_left(window, nums[i-k]))
            insort(window, nums[i])


        return med
    

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        is_odd = k%2
        window = sorted(nums[:k])

        ans = []

        for i in range(k,len(nums)+1):
            if is_odd:
                ans.append(window[k//2])

            else:
                med = window[k//2-1] + window[k//2]
                ans.append(med/2)

            if i == len(nums):
                break

            window.pop(bisect_left(window,nums[i-k]))
            insort(window, nums[i])

        return ans
    

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        is_odd = k%2

        ans = []

        for i in range(k, len(nums)+1):
            if is_odd:
                ans.append(window[k//2])

            else:
                med = window[k//2-1] + window[k//2]
                ans.append(med/2)

            if i == len(nums):
                break

            window.pop(bisect_left(window, nums[i-k]))
            insort(window, nums[i])

        
        return ans
