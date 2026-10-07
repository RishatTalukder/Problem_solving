# Intuition

The main idea is to use a stack to keep track of the **indices of unmatched parentheses**.

Instead of storing the characters themselves, we store their indices. This allows us to calculate the length of a valid substring using:

```text
current_index - index_of_last_unmatched_character
```

We initialize the stack with `-1`. This acts as a **base index** for a valid substring that starts from index `0`.

# Approach

Traverse the string from left to right.

* When we see `(`, push its index onto the stack because it may need to be matched later.
* When we see `)`, pop the top of the stack because we have found a matching opening parenthesis.

After popping:

* If the stack becomes empty, it means this `)` has no matching `(`. We push its index as the new boundary.
* Otherwise, the current valid substring ends at `i`, and its length is:

```text
i - stack[-1]
```

We update `ans` with the maximum length found.

For example:

```text
s = "()(())"
```

The initial stack is:

```text
[-1]
```

After processing the valid pairs, the indices stored in the stack represent the boundaries of the current valid substring. Whenever we find a valid closing parenthesis, subtracting the top index from the current index gives the length of the valid substring ending at that position.

The `-1` sentinel is important because for a string like:

```text
()
```

when we reach index `1`, the stack becomes:

```text
[-1]
```

so:

```text
1 - (-1) = 2
```

which correctly gives the length of the valid substring.

# Complexity

* Time complexity: `O(n)`

  We traverse the string once, and every index is pushed and popped at most once.

* Space complexity: `O(n)`

  In the worst case, the stack can contain the indices of all opening parentheses.

# Code

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]

        ans = 0

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)

                else:
                    ans = max(ans, i - stack[-1])

        return ans
```
