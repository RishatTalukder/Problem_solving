class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        fac = []

        for i in range(1, isqrt(n)+1):
            if n%i == 0:
                fac.append(i)
                
                if n//i != i:
                    fac.append(n // i)

        target = sorted(nums)

        def kmp(val, pat):
            n, m = len(val), len(pat)

            lps = [0]*m

            j = 0

            for i in range(1, m):
                while j > 0 and pat[i] != pat[j]:
                    j = lps[j-1]

                if pat[i] == pat[j]:
                    j += 1

                lps[i] = j


            j = 0

            for i in range(n):
                while j > 0 and val[i] != pat[j]:
                    j = lps[j-1]

                if val[i] == pat[j]:
                    j += 1

                if j == m:
                    return True


            return False


        def check(nums1, nums2):
            return kmp(nums1+nums1, nums2)

        ans = 0

        for d in fac:
            for left in range(0,n,d):
                right = left + d

                if not check(nums[left: right], target[left: right]):
                    break

            else:
                ans += d


        return ans