# Intuition

We need to repeatedly divide the string into groups of size `k`, calculate the sum of each group's digits, and concatenate those sums to form a new string.

The important detail is that a group's digit sum isn't necessarily a single digit. For example, `"91"` produces `10`, which contributes two digits (`'1'` and `'0'`) to the next round.

We can use a queue to process the digits in their original order, consuming `k` digits at a time until the entire current string has been processed.

We repeat this process until the resulting string has at most `k` characters.

# Approach

1. Convert the input string into a deque of integers so we can efficiently remove digits from the front.
2. While the deque contains more than `k` digits:
   - Create an empty list to store the digits of the next string.
   - Process the deque in groups of at most `k` elements.
   - Calculate the sum of each group.
   - Convert the sum into a string, then convert its individual characters back into integers.
   - Extend the result list with those digits.
3. Once the current string has at most `k` digits, join the remaining digits and return the final string.

Using `deque.popleft()` allows us to consume the digits from left to right while preserving their order.

# Complexity

- Time complexity: \(O(n \log n)\) — Each round processes every digit in the current string. Since every group contains at least two digits (\(k \geq 2\)), the string length decreases by at least a constant factor in each round. Therefore, there are \(O(\log n)\) rounds, with at most \(O(n)\) work per round.

- Space complexity: \(O(n)\) — We store the current digits in a deque and the newly generated digits in a list. Both require at most linear space relative to the original string length.

# Code

```python
from collections import deque

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        q = deque(map(int, list(s)))

        while len(q) > k:
            summ = []

            while q:
                batch = []

                for i in range(k):
                    if q:
                        batch.append(q.popleft())
                    else:
                        break

                batch = list(map(int, str(sum(batch))))
                summ.extend(batch)

            q = deque(summ)

        return ''.join(map(str, list(q)))
```