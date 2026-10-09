# Scoring Parentheses Using a Stack

## Intuition

The key to solving this problem is understanding how the score of a valid parentheses string is calculated:

* `()` has a score of `1`.
* `AB` has a score of `A + B`, where `A` and `B` are valid parentheses strings.
* `(A)` has a score of `2 * A`.

The tricky part is handling nested parentheses. For example, `(()())` contains two inner pairs, each contributing `1`. Since they are inside another pair, their combined score is doubled:

`(()()) = 2 * (1 + 1) = 4`

We can use a stack to keep track of the scores of nested parentheses. Instead of storing the actual brackets, we store the scores of the groups we're currently processing.

## Approach

We initialize the stack with `[0]`. This initial `0` acts as the score accumulator for the outermost level of the string.

Then, we iterate through each character:

1. **When we encounter `(`:**

   We push `0` onto the stack. This represents a new, empty parentheses group whose score we haven't calculated yet.

2. **When we encounter `)`:**

   We pop the top value from the stack. This value represents the score accumulated inside the matching opening parenthesis.

   * If the value is `0`, the group is an empty pair `()`, so its score is `1`.
   * Otherwise, the group contains another valid parentheses string, so its score is doubled.

   Finally, we add the calculated score to the new top of the stack. This combines the completed group's score with any other groups at the same nesting level.

3. **Return the final score:**

   After processing every character, the stack's bottom element contains the total score of the entire string.

### Example walkthrough

Let's consider `s = "(()())"`.

| Character | Action                                           | Stack          |
| --------- | ------------------------------------------------ | -------------- |
| Start     | Initialize the stack                             | `[0]`          |
| `(`       | Push `0`                                         | `[0, 0]`       |
| `(`       | Push `0`                                         | `[0, 0, 0]`    |
| `)`       | Empty pair scores `1`; add it to parent          | `[0, 0, 1]`    |
| `(`       | Push `0`                                         | `[0, 0, 1, 0]` |
| `)`       | Empty pair scores `1`; add it to parent          | `[0, 0, 1, 1]` |
| `)`       | Inner group scores `1 + 1 = 2`; double it to `4` | `[0, 4]`       |
| `)`       | The outer group scores `4`                       | `[4]`          |

The final answer is `4`.

**Why does this work?**

Every time we encounter a closing parenthesis, we finish calculating one group. We either assign it a score of `1` if it is an empty pair, or double its accumulated score if it contains nested groups. By adding that score to the enclosing group, we naturally handle both nesting and adjacent parentheses.

## Complexity

* **Time complexity:** \(O(n)\), where \(n\) is the length of the string. Each character is processed once, and each opening parenthesis is pushed and popped at most once.
* **Space complexity:** \(O(n)\) in the worst case, when the string contains deeply nested parentheses and the stack grows proportionally to its length.

## Code

```python3
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                curr = stack.pop()

                if curr == 0:
                    curr = 1
                else:
                    curr *= 2

                stack[-1] += curr

        return stack[-1]
```
