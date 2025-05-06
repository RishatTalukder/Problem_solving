class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = 2 * n - 1
        result = [0] * length
        used = [False] * (n + 1)  # Track which numbers are used

        self.backtrack(result, used, n, 0)
        return result

    def backtrack(self, result: List[int], used: List[bool], n: int, index: int) -> bool:
        # Skip already filled positions
        while index < len(result) and result[index] != 0:
            index += 1
        
        # If we have filled the entire array, we are done
        if index == len(result):
            return True

        # Try placing numbers from n down to 1 to get lexicographically larger sequence
        for num in range(n, 0, -1):
            if used[num]:
                continue

            # Case 1: Place `1` (only one occurrence allowed)
            if num == 1:
                result[index] = 1
                used[1] = True

                if self.backtrack(result, used, n, index + 1):
                    return True

                # Backtrack
                result[index] = 0
                used[1] = False

            # Case 2: Place number `num` at `index` and `index + num`
            elif index + num < len(result) and result[index] == 0 and result[index + num] == 0:
                result[index] = num
                result[index + num] = num
                used[num] = True

                if self.backtrack(result, used, n, index + 1):
                    return True

                # Backtrack
                result[index] = 0
                result[index + num] = 0
                used[num] = False

        # No valid placement found at this position
        return False
