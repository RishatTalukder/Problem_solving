# Intuition

We need to generate every possible valid sequence of `n` pairs of parentheses.

The important part is that we should **never build an invalid sequence in the first place**.

At any point, we can add:

* `(` as long as we haven't used all `n` opening parentheses.
* `)` only when there are more opening parentheses than closing parentheses already used.

This guarantees that every sequence we generate is valid.

# Approach

We use recursion to build the string one character at a time.

We keep track of:

* `open` — number of `(` currently used.
* `close` — number of `)` currently used.
* `s` — the current parentheses sequence.

There are two possible choices at every step.

### Add `(`

If:

```python
open < n
```

we can safely add another opening parenthesis:

```python
dp(open + 1, close, s + '(')
```

### Add `)`

We can only add a closing parenthesis if:

```python
close < open
```

This prevents us from creating an invalid prefix such as:

```text
)(
```

or:

```text
())...
```

before enough opening parentheses have been added.

### Base case

When both counts reach `n`:

```python
open == n and close == n
```

we have constructed one complete valid sequence, so we add it to `ans`.

This effectively explores all valid combinations while pruning invalid ones along the way.

# Complexity

There are `Cₙ` valid combinations, where `Cₙ` is the `n`th Catalan number.

* Time complexity: `O(Cₙ × n)`

  We generate `Cₙ` valid strings, each containing `2n` characters.

* Space complexity: `O(Cₙ × n)`

  This accounts for storing all generated strings. The recursion itself uses `O(n)` stack space.

# Code

```python3 id="7m3qk1"
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        ans = []

        def dp(open, close, s):

            if open == n and close == n:
                ans.append(s)
                return

            if open < n:
                dp(open + 1, close, s + '(')

            if close < open:
                dp(open, close + 1, s + ')')

        dp(0, 0, '')

        return ans
```
