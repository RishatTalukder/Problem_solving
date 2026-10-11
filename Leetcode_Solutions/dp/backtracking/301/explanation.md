# Removing Invalid Parentheses Using Backtracking

## Intuition

The goal is to remove the minimum number of parentheses to make the string valid while keeping all non-parenthesis characters unchanged.

Instead of deciding in advance which parentheses to remove, we can explore both possibilities for every parenthesis:

- **Keep it:** Include the parenthesis in our current string and update the balance.
- **Remove it:** Skip the parenthesis and continue without changing the balance.

We use a variable called `count` to track the balance between opening and closing parentheses. Every `(` increases the balance by one, while every `)` decreases it by one.

There are two important observations:

- If `count` becomes negative, we have encountered more closing parentheses than opening parentheses. This string cannot become valid by adding more characters, so we can stop exploring that branch.
- At the end of the string, `count` must be zero for the resulting string to be valid.

However, there can be multiple valid strings. We need to return **all valid strings that retain the maximum number of characters**, which means removing the minimum number of parentheses.

To handle this, we maintain `maxln`, the length of the longest valid string found so far, and a set called `res` to store all valid strings of that length.

## Approach

We solve the problem using backtracking, exploring the choices for each character recursively.

### 1. Initialize the variables

- `n` stores the length of the input string.
- `res` is a set that stores the longest valid strings found so far. Using a set also prevents duplicate results.
- `maxln` tracks the maximum length of any valid string discovered.

Our recursive function `solve(s, i, cur, count)` uses:

- `i`: The current index in the input string.
- `cur`: A list containing the characters we have decided to keep.
- `count`: The current parentheses balance.

### 2. Prune invalid branches

At the beginning of each recursive call, we check whether `count` is negative.

If it is, we return immediately because the current string has more closing parentheses than opening parentheses. Removing characters later cannot fix this imbalance in the prefix we have already kept.

This prevents us from exploring branches that cannot produce a valid answer.

### 3. Handle the end of the string

When `i == n`, we have processed every character.

If `count == 0`, the current string is valid.

Now we compare its length with `maxln`:

- **If `len(cur) > maxln`:** We have found a longer valid string. We clear the previous results, add the current string, and update `maxln`.
- **If `len(cur) == maxln`:** We add the current string to `res` because it is another valid answer with the same maximum length.
- **If `len(cur) < maxln`:** We ignore it because it requires removing more characters than the best solutions already found.

This ensures that we only return valid strings with the maximum possible length.

### 4. Handle non-parenthesis characters

If `s[i]` is neither `(` nor `)`, we must preserve it.

We append the character to `cur`, recursively process the next index, and then remove the character from `cur` using `pop()`.

That final `pop()` is essential: it restores the previous state before the next recursive call.

### 5. Explore both choices for a parenthesis

For each parenthesis, we explore two branches.

**Branch A: Keep the parenthesis**

We append `s[i]` to `cur` and update the balance:

- For `(`, increment `count`.
- For `)`, decrement `count`.

Then we recursively process the next character. Once that branch finishes, we remove the current parenthesis from `cur` to restore the previous state.

**Branch B: Remove the parenthesis**

We skip the current character and recursively process the next index without changing `cur` or `count`.

By exploring both choices, we consider every possible way of removing parentheses. The pruning condition eliminates branches that cannot produce valid strings.

Finally, we return `list(res)` to convert the set of unique longest valid strings into a list.

## Complexity

Let \(n\) be the length of the input string.

- **Time complexity:** \(O(n \cdot 2^n)\) in the worst case. Each parenthesis has two choices: keep or remove. There can be up to \(2^n\) combinations to explore, and constructing or storing a resulting string can take \(O(n)\) time.

- **Space complexity:** \(O(n \cdot 2^n)\) in the worst case, including the recursion stack, the current character list, and the set of valid results. The recursion depth and current list are each \(O(n)\), while storing exponentially many result strings can require \(O(n \cdot 2^n)\) space.

## Code

```python3
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        res = set()
        maxln = 0

        def solve(s, i, cur, count):
            nonlocal maxln

            if count < 0:
                return

            if i == n:
                if count == 0:
                    if len(cur) > maxln:
                        res.clear()
                        res.add(''.join(cur))
                        maxln = len(cur)

                    elif len(cur) == maxln:
                        res.add(''.join(cur))

                return

            if s[i] not in '()':
                cur.append(s[i])
                solve(s, i + 1, cur, count)
                cur.pop()
                return

            cur.append(s[i])

            solve(
                s,
                i + 1,
                cur,
                count + (1 if s[i] == '(' else -1)
            )

            cur.pop()

            solve(
                s,
                i + 1,
                cur,
                count
            )

        solve(s, 0, [], 0)

        return list(res)
```

