class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1  # Number of digits in the current range
        range_start = 1  # Starting number of the current range
        
        # Determine the range in which the nth digit falls
        while n > 9 * range_start * digit_length:
            n -= 9 * range_start * digit_length
            digit_length += 1
            range_start *= 10
        
        # Find the exact number and digit within that number
        number_index, digit_index = divmod(n - 1, digit_length)
        target_number = range_start + number_index
        target_digit = str(target_number)[digit_index]
        
        return int(target_digit)

# Example usage
Sol = Solution()
print(Sol.findNthDigit(1234))  # Output: 4