# Intuition

We need to find how many parentheses are missing to make the string valid.

While traversing the string, we can use a stack to keep track of unmatched opening parentheses `(`.

Whenever we encounter a closing parenthesis `)`:

* If there is an unmatched `(` in the stack, we match them by popping it.
* Otherwise, this `)` has no matching `(`, so we need to add an opening parenthesis. We keep track of this using `count`.

After processing the entire string, any `(` remaining in the stack also needs a corresponding `)`.

Therefore, the answer is:

```text
unmatched closing parentheses + unmatched opening parentheses
```

# Approach

Traverse the string from left to right.

* For `(`, push it onto the stack.
* For `)`:

  * If the stack is not empty, pop one `(` because they form a valid pair.
  * Otherwise, increment `count` because we need to add a `(` before this `)`.

After the loop, `len(stack)` represents the number of unmatched `(` remaining, so we need that many `)`.

Therefore:

```python
count + len(stack)
```

is the minimum number of additions required.

# Complexity

* Time complexity: `O(n)`

* Space complexity: `O(n)`

# Code

```python3
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        count = 0

        for ch in s:

            if ch == '(':
                stack.append(ch)

            else:
                if stack:
                    stack.pop()

                else:
                    count += 1

        return count + len(stack)
```
