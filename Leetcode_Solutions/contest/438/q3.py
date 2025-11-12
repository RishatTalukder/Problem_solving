from collections import deque


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        stack = deque(map(int, s))

        while len(stack) > 2:
            new_s = deque()
            for i in range(len(stack) - 1):
                new_s.append((stack[i] + stack[i + 1]) % 10)

            stack = new_s

        return stack[0] == stack[1]
    


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(map(int, s))  # Convert string to digit list
        n = len(s)

        # Compute final two digits directly
        a, b = 0, 0
        coeff_a, coeff_b = 1, 1  # Pascal's Triangle coefficients mod 10

        for i in range(n):
            if i % 2 == 0:
                a = (a + coeff_a * s[i]) % 10
                coeff_a = (coeff_a * (n - i - 1) // (i + 1)) % 10
            else:
                b = (b + coeff_b * s[i]) % 10
                coeff_b = (coeff_b * (n - i - 1) // (i + 1)) % 10

        return a == b


sol = Solution()
print(sol.hasSameDigits('3902'))