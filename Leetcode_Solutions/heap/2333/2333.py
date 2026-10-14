class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        ans = 0

        maxx = 0

        for i in range(len(nums1)):
            maxx = max(maxx, abs(
                nums1[i] - nums2[i]
            ))

        
        freq = [0]*(maxx+ 1)

        for i in range(len(nums1)):
            freq[abs(
                nums1[i] - nums2[i]
            )] += 1


        for i in range(maxx, 0, -1):
            if k <= 0:
                break

            minn = min(k, freq[i])

            k -= minn
            freq[i] -= minn
            freq[i-1] += minn


        for i in range(maxx, 0, -1):
            ans += i*i*freq[i]


        return ans