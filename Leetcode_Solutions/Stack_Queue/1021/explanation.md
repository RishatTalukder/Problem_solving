# Removing Outer Parentheses Using Depth Tracking

## Intuition

A primitive parentheses string is a non-empty valid parentheses string that cannot be split into two smaller non-empty valid parentheses strings.

For example, `"(()())"` is a primitive string. Its outermost parentheses are the first `(` and the last `)`. Removing them leaves `"()()"`.

The key observation is that we can identify these outermost parentheses by tracking the **nesting depth** of the string.

- When we encounter `(`, the depth increases.
- When we encounter `)`, the depth decreases.

The outermost opening parenthesis appears when the depth is `0` before we process it. Similarly, the outermost closing parenthesis is the one that brings the depth back to `0`.

We can use this depth to decide which characters to include in our answer without using a stack.

## Approach

We initialize two variables:

- `depth = 0` to track the current nesting depth.
- `ans = ''` to store the parentheses we want to keep.

Then, we iterate through every character in the string.

### 1. Update the depth before processing a closing parenthesis

If the current character is `)`, we decrease `depth` first.

This is important because we want to exclude the outermost closing parenthesis. When it brings the depth down to `0`, we know it closes the primitive string, so we should not include it in the answer.

### 2. Add the character only when the depth is not zero

After handling a possible closing parenthesis, we check whether `depth != 0`.

- If the depth is not zero, the current character belongs to the inside of a primitive string, so we add it to `ans`.
- If the depth is zero, the current character is an outermost parenthesis, so we skip it.

### 3. Update the depth after processing an opening parenthesis

If the current character is `(`, we increase `depth` after checking whether to add the character.

This ensures that an outermost opening parenthesis is excluded because the depth is still `0` when we check it.

### Example walkthrough

Consider `s = "(()())(())"`.

| Character | Depth after initial update | Added to answer? | Answer |
|---|---:|---|---|
| `(` | 0 | No | `""` |
| `(` | 1 | Yes | `"("` |
| `)` | 1 | Yes | `"()"` |
| `(` | 1 | Yes | `"()("` |
| `)` | 1 | Yes | `"()()"` |
| `)` | 0 | No | `"()()"` |
| `(` | 0 | No | `"()()"` |
| `(` | 1 | Yes | `"()()("` |
| `)` | 1 | Yes | `"()()()"` |
| `)` | 0 | No | `"()()()"` |

The final answer is `"()()()"`.

Notice how the depth determines whether a parenthesis is an outermost one or belongs to the inside of a primitive string.

## Complexity

- **Time complexity:** \(O(n)\), where \(n\) is the length of the input string. We traverse each character exactly once.

- **Space complexity:** \(O(n)\) for the resulting string in the worst case. The depth variable itself uses \(O(1)\) auxiliary space. Strictly speaking, repeated string concatenation with `ans += ch` can take \(O(n^2)\) time in Python because strings are immutable; using a list and `''.join()` would guarantee linear-time construction.

## Code

```python3
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        ans = ''

        for ch in s:
            if ch == ')':
                depth -= 1

            if depth != 0:
                ans += ch

            if ch == '(':
                depth += 1

        return ans
```