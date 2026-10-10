# Minimum Additions to Balance Parentheses Using a Stack

## Intuition

The idea is to count how many parentheses we need to add to make the string valid.

A valid parentheses string must satisfy two conditions:

- Every opening parenthesis `(` must have a matching closing parenthesis `)`.
- A closing parenthesis `)` cannot appear without a matching opening parenthesis before it.

For example, consider `s = "())"`.

The first `(` matches the first `)`, but the last `)` has no matching opening parenthesis. We need to add one `(` to make the string valid, resulting in `"()()"`.

To solve this, we can use a stack to keep track of unmatched opening parentheses and a counter for unmatched closing parentheses.

## Approach

We initialize an empty stack and a counter `count = 0`.

Then, we iterate through each character in the string.

1. **If the character is `(`:**

   We push it onto the stack because we need a corresponding `)` to match it later.

2. **If the character is `)`:**

   - If the stack is not empty, there is an unmatched opening parenthesis available. We pop it from the stack because the pair is now balanced.
   - If the stack is empty, there is no opening parenthesis available to match this `)`. Therefore, we must add an extra `(`, so we increment `count`.

3. **Calculate the final answer:**

   After processing the entire string, `count` tells us how many opening parentheses we need to add for unmatched closing parentheses.

   However, the stack may still contain unmatched opening parentheses. Each of these requires an additional closing parenthesis.

   Therefore, the minimum number of additions is:

   `count + len(stack)`

### Example walkthrough

Let's consider `s = "()))(("`.

| Character | Action | Stack | Count |
|---|---|---|---|
| Start | Initialize | `[]` | `0` |
| `(` | Push opening parenthesis | `['(']` | `0` |
| `)` | Match and pop | `[]` | `0` |
| `)` | No opening parenthesis; increment count | `[]` | `1` |
| `)` | No opening parenthesis; increment count | `[]` | `2` |
| `(` | Push opening parenthesis | `['(']` | `2` |
| `(` | Push opening parenthesis | `['(', '(']` | `2` |

At the end, `count = 2` and `len(stack) = 2`.

So the answer is:

\[
2 + 2 = 4
\]

We need two opening parentheses to match the unmatched closing parentheses and two closing parentheses to match the remaining opening parentheses.

## Complexity

- **Time complexity:** \(O(n)\), where \(n\) is the length of the string. We traverse the string once, and each character requires constant-time work.

- **Space complexity:** \(O(n)\) in the worst case, because the stack may contain all the opening parentheses if the string consists entirely of `(` characters.

## Code

```python3
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0

        for ch in s:
            if ch == '(':
                stack.append(ch)

            else:
                if not stack:
                    count += 1

                else:
                    stack.pop()

        return count + len(stack)
```