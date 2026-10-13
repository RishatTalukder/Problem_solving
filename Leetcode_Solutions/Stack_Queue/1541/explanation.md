# Minimum Insertions to Balance Parentheses Using Greedy Matching

## Intuition

Unlike the usual parentheses problems, where every opening parenthesis `(` needs just one closing parenthesis `)`, this problem has a different rule:

**Every `(` must be matched with exactly two consecutive closing parentheses `))`.**

For example:

- `())` is valid because the opening parenthesis is followed by two closing parentheses.
- `(()))` is valid because the first `(` is matched by the next two `)`, and the second `(` is matched by the final two `)`.
- `(()` is invalid because the opening parenthesis does not have enough closing parentheses.

Our goal is to find the minimum number of insertions needed to make the string valid. We can insert either `(` or `)` anywhere in the string.

The key idea is to process the string from left to right and greedily match each opening parenthesis with its required pair of closing parentheses.

We maintain two variables:

- `left`: The number of opening parentheses that still need to be matched.
- `count`: The number of insertions we need to make so far.

We also use an index `i` to examine the string. Since a valid match requires two consecutive `)` characters, we sometimes need to inspect two characters at once.

## Approach

### 1. Initialize the variables

We start with:

- `left = 0`, because initially there are no unmatched opening parentheses.
- `count = 0`, because we haven't inserted anything yet.
- `i = 0`, to track our current position in the string.

### 2. If the current character is `(`

We increment `left` because this opening parenthesis needs two closing parentheses to match it.

Then, we move `i` forward by one to process the next character.

For example, if we encounter `"("`, we now have one unmatched opening parenthesis, so `left = 1`.

### 3. If the current character is `)`

We need to determine whether the current `)` is followed by another `)`.

There are two possible cases.

**Case A: The next character is also `)`**

We have a complete pair of closing parentheses, `))`.

- If `left > 0`, we have an unmatched opening parenthesis that can use this pair. We decrement `left` to mark that opening parenthesis as matched.
- If `left == 0`, there is no opening parenthesis available for this pair. We need to insert one `(` before the pair, so we increment `count` by one.

In either situation, we move `i` forward by two because we have processed both closing parentheses.

For example, consider `"())"`:

- The first `(` makes `left = 1`.
- The next two characters are `))`, which match that opening parenthesis.
- No insertions are needed, so the answer is `0`.

**Case B: The next character is not `)` or there is no next character**

The current `)` does not have a second consecutive closing parenthesis.

We need to insert one `)` immediately after it to complete the required pair.

Therefore, we increment `count` by one.

Now we have a complete pair of closing parentheses, so we need to match it with an opening parenthesis:

- If `left > 0`, we decrement `left` because one opening parenthesis has now been matched.
- If `left == 0`, there is no opening parenthesis available. We must insert one `(` as well, so we increment `count` again.

Finally, we move `i` forward by one. We only advance past the original character because the next character, if present, still needs to be processed.

### 4. Count the remaining unmatched opening parentheses

After processing the entire string, `left` represents the number of opening parentheses that still need to be matched.

Each remaining `(` requires two closing parentheses, so we need two insertions per unmatched opening parenthesis.

Therefore, the final answer is:

\[
\text{count} + 2 \times \text{left}
\]

The `count` variable accounts for insertions already made while processing the string, while `2 * left` accounts for the missing closing parentheses of any remaining opening parentheses.

### Example walkthrough

Let's consider `s = "(()))"`.

| Step | Character(s) processed | `left` | `count` | Explanation |
|---|---|---:|---:|---|
| 1 | `(` | 1 | 0 | An opening parenthesis needs two closing parentheses. |
| 2 | `(` | 2 | 0 | Another opening parenthesis needs two closing parentheses. |
| 3 | `))` | 1 | 0 | The pair matches one opening parenthesis. |
| 4 | `)` | 0 | 1 | Only one `)` remains, so insert another `)` to complete its pair. |

At the end, `left = 0` and `count = 1`.

The answer is:

\[
1 + 2(0) = 1
\]

We need one insertion to turn `"(()))"` into a valid string. For example, inserting `(` at the beginning produces `"((()))"`, which is valid.

## Complexity

- **Time complexity:** \(O(n)\), where \(n\) is the length of the string. We traverse the string from left to right. Each iteration advances the index by either one or two, so each character is processed at most once.

- **Space complexity:** \(O(1)\), because we only use three variables: `left`, `count`, and `i`. We do not use an additional data structure whose size grows with the input.

## Code

```python3
class Solution:
    def minInsertions(self, s: str) -> int:
        left = 0
        count = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                left += 1
                i += 1

            else:
                if i + 1 < len(s) and s[i + 1] == ")":
                    if left > 0:
                        left -= 1
                    else:
                        count += 1

                    i += 2

                else:
                    count += 1

                    if left > 0:
                        left -= 1
                    else:
                        count += 1

                    i += 1

        return count + left * 2
```

