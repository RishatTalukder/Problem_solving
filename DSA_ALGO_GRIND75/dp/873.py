class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set = set(arr)
        mx_ln = 0
        n = len(arr)

        for start in range(n):
            for next in range(start+1,n):
                prev = arr[next]
                curr = arr[start] + prev
                curr_ln = 2

                while curr in num_set:
                    prev, curr = curr, prev + curr
                    curr_ln += 1
                    mx_ln = max(mx_ln, curr_ln)

        return mx_ln if mx_ln > 2 else 0