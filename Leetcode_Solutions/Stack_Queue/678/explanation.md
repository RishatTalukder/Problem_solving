# Intuition

The `*` character makes this problem different from normal valid-parentheses problems because it can represent:

* `(`
* `)`
* an empty string

Instead of trying all three possibilities, we can delay deciding what each `*` represents.

We maintain two stacks:

* `stack` stores the indices of unmatched `(`.
* `stars` stores the indices of `*`.

When we encounter a `)`:

1. If there is an unmatched `(`, use it to match the `)`.
2. Otherwise, use a `*` as `(`.
3. If neither is available, the string cannot be valid.

The important part is that we store **indices**, not just the characters. This becomes necessary when dealing with unmatched `(` after the first pass.

# Approach

Traverse the string from left to right.

### Opening parenthesis

For `(`, store its index:

```python
stack.append(i)
```

because it needs to be matched by a future `)` or `*`.

### Star

For `*`, store its index separately:

```python
stars.append(i)
```

We don't decide what the `*` represents yet.

### Closing parenthesis

For `)`:

* If `stack` is not empty, match it with the most recent `(`.
* Otherwise, if `stars` is not empty, use the most recent `*` as an opening parenthesis.
* If both are empty, there is no way to match this `)`.

After the first pass, we may still have unmatched `(`.

We can potentially use `*` characters that appeared **after** those `(` as closing parentheses.

This is why we compare their indices:

```python
if stack.pop() > stars.pop():
    return False
```

For example:

```text
(*)
```

The `(` comes before `*`, so the `*` can act as `)`:

```text
( * )
```

But consider:

```text
*( 
```

The `*` comes before `(`. It cannot act as a closing parenthesis for that `(` because that would require the closing parenthesis to appear before the opening one.

Therefore, when matching remaining `(` with `*`, the `*` must have a **larger index** than the `(`.

If we successfully match all remaining opening parentheses with later `*` characters, then the string can be made valid.

# Complexity

* Time complexity: `O(n)`

  We traverse the string once, and the second `while` loop processes each stored index at most once.

* Space complexity: `O(n)`

  In the worst case, all characters can be stored in one of the two stacks.

# Code

```python3
class Solution:
    def checkValidString(self, s: str) -> bool:

        stack = []
        stars = []

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            elif ch == '*':
                stars.append(i)

            else:
                if stack:
                    stack.pop()

                elif stars:
                    stars.pop()

                else:
                    return False

        while stack and stars:

            if stack.pop() > stars.pop():
                return False

        return not stack
```
