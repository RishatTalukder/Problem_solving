class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = n = len(words)

        for i, num in enumerate(words):
            if num == target:
                ans = min(ans, abs(i- startIndex), n- abs(i-startIndex))

        return ans if ans < n else -1