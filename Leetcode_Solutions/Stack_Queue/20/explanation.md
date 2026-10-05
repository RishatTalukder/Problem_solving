# Valid Parentheses — Solution Explanation

The idea behind this solution is to use a **stack** to keep track of the closing brackets that we are expecting.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for ch in s:
            if ch not in brackets:
                if not stack:
                    return False

                if stack.pop() != ch:
                    return False

            elif ch in brackets:
                stack.append(brackets[ch])

        
        return not stack
```

---

## 1. What does "valid" mean?

A string of brackets is valid when:

1. Every opening bracket has a corresponding closing bracket.
2. The brackets must be closed in the correct order.
3. A closing bracket cannot appear without its corresponding opening bracket.

For example:

```text
()
```

is valid.

```text
({[]})
```

is valid.

But:

```text
([)]
```

is invalid because `[` was opened after `(`, so it must be closed before `(`.

---

# 2. The main idea

The important observation is:

> Whenever we see an opening bracket, we know exactly which closing bracket we expect to see later.

For example:

```text
(
```

means that eventually we expect:

```text
)
```

Similarly:

```text
{
```

expects:

```text
}
```

and:

```text
[
```

expects:

```text
]
```

Your dictionary represents exactly this relationship:

```python
brackets = {
    '(' : ')',
    '{' : '}',
    '[' : ']'
}
```

So instead of storing the opening brackets, the solution stores the **closing brackets that are expected**.

---

# 3. Why use a stack?

A stack follows the **LIFO** principle:

> Last In, First Out.

That is exactly what nested brackets require.

Consider:

```text
({[]})
```

When we encounter the opening brackets:

```text
(
(
{
(
{
[
```

The most recently opened bracket must be closed first.

So the expected closing brackets become:

```text
)
}
]
```

Inside the stack:

```text
stack = [')', '}', ']']
```

When we encounter `]`, we need to check the **most recently expected closing bracket**.

That's exactly what:

```python
stack.pop()
```

does.

It removes and returns the last element:

```text
stack = [')', '}']
             ^
             |
          pop this
```

This makes a stack a natural data structure for the problem.

---

# 4. Starting with an empty stack

```python
stack = []
```

Initially, we aren't expecting any closing brackets.

As we encounter opening brackets, we add their corresponding closing brackets to the stack.

---

# 5. Iterating through the string

```python
for ch in s:
```

We process the string one character at a time.

There are essentially two cases:

```text
Opening bracket
        ↓
   Add expected
 closing bracket
   to the stack


Closing bracket
        ↓
Check it against
the top of stack
```

---

# 6. Handling an opening bracket

This part handles opening brackets:

```python
elif ch in brackets:
    stack.append(brackets[ch])
```

Suppose:

```python
ch = '('
```

Since `(` is a key in `brackets`:

```python
brackets['(']
```

gives:

```text
')'
```

So:

```python
stack.append(brackets[ch])
```

becomes effectively:

```python
stack.append(')')
```

Now:

```text
stack = [')']
```

For:

```text
({[
```

the process looks like:

```text
ch = '('
stack = [')']

ch = '{'
stack = [')', '}']

ch = '['
stack = [')', '}', ']']
```

Notice that we aren't storing:

```text
( { [
```

We're storing:

```text
) } ]
```

because those are the characters we're expecting next.

---

# 7. Handling a closing bracket

If the character isn't an opening bracket:

```python
if ch not in brackets:
```

then this solution treats it as a closing bracket.

For example:

```text
)
}
]
```

---

## First check: Is the stack empty?

```python
if not stack:
    return False
```

This handles cases where a closing bracket appears without any opening bracket.

For example:

```text
]
```

We encounter `]`.

The stack is empty:

```text
stack = []
```

There is nothing that could have produced an expected `]`.

Therefore:

```python
return False
```

This also handles:

```text
)
```

and:

```text
}
```

---

# 8. Comparing with the expected closing bracket

The most important line is:

```python
if stack.pop() != ch:
    return False
```

Remember that the stack contains the closing brackets we are expecting.

Suppose we have:

```text
({[]})
```

After processing:

```text
({
```

the stack is:

```text
[')', '}', ']']
```

Now we encounter:

```text
]
```

We execute:

```python
stack.pop()
```

which gives:

```text
']'
```

Then:

```python
']' != ']'
```

is:

```python
False
```

So everything is fine.

The stack becomes:

```text
[')', '}']
```

---

# 9. Why `pop()` is exactly what we want

Consider:

```text
([{}])
```

After reading:

```text
([
```

we have:

```text
stack = [')', ']', '}']
```

The next character is:

```text
}
```

The top of the stack is:

```text
}
```

So it matches.

Then the stack becomes:

```text
[')', ']']
```

Next:

```text
]
```

matches the top:

```text
]
```

Then:

```text
)
```

matches:

```text
)
```

Everything closes in reverse order of opening.

That's precisely how nested structures work.

---

# 10. Detecting incorrectly ordered brackets

Consider:

```text
([)]
```

Let's process it.

### First character

```text
(
```

Expected:

```text
)
```

Stack:

```text
[')']
```

### Second character

```text
[
```

Expected:

```text
]
```

Stack:

```text
[')', ']']
```

### Third character

```text
)
```

Now:

```python
stack.pop()
```

returns:

```text
]
```

But the current character is:

```text
)
```

So:

```python
']' != ')'
```

is true.

Therefore:

```python
return False
```

This is how the solution catches incorrectly nested brackets.

---

# 11. Why the final `return not stack` works

After processing the entire string:

```python
return not stack
```

This checks whether the stack is empty.

In Python:

```python
not []
```

is:

```text
True
```

while:

```python
not [')']
```

is:

```text
False
```

So:

```python
return not stack
```

essentially means:

> "Return `True` only if we have no unmatched opening brackets left."

For example:

```text
()
```

Processing:

```text
(
stack = [')']

)
stack = []
```

At the end:

```python
not stack
```

becomes:

```python
not []
```

which is:

```text
True
```

---

# 12. Detecting missing closing brackets

Consider:

```text
(((
```

Processing it gives:

```text
(
stack = [')']

(
stack = [')', ')']

(
stack = [')', ')', ')']
```

The string ends.

There are still three expected closing brackets in the stack.

Therefore:

```python
not stack
```

is:

```python
not [')', ')', ')']
```

which is:

```text
False
```

So the string is invalid.

---

# 13. Complete walkthrough

Let's take:

```text
s = "{[()]}"
```

We can visualize the execution like this:

| Character | Type    | Operation | Stack             |
| --------- | ------- | --------- | ----------------- |
| `{`       | Opening | Push `}`  | `['}']`           |
| `[`       | Opening | Push `]`  | `['}', ']']`      |
| `(`       | Opening | Push `)`  | `['}', ']', ')']` |
| `)`       | Closing | Pop `)`   | `['}', ']']`      |
| `]`       | Closing | Pop `]`   | `['}']`           |
| `}`       | Closing | Pop `}`   | `[]`              |

At the end:

```python
return not stack
```

becomes:

```python
return not []
```

which returns:

```text
True
```

---

# 14. Another walkthrough: invalid input

Consider:

```text
s = "{[(])}"
```

| Character | Operation             | Stack             |
| --------- | --------------------- | ----------------- |
| `{`       | Push `}`              | `['}']`           |
| `[`       | Push `]`              | `['}', ']']`      |
| `(`       | Push `)`              | `['}', ']', ')']` |
| `]`       | Expected `)`, got `]` | Invalid           |

At `]`:

```python
stack.pop()
```

returns:

```text
)
```

but:

```python
ch
```

is:

```text
]
```

Therefore:

```python
')' != ']'
```

and we immediately return:

```python
False
```

---

# 15. Why the dictionary stores closing brackets

There are two common ways to implement this problem.

You could store opening brackets:

```python
stack.append(ch)
```

and then use another dictionary to determine which opening bracket corresponds to a closing bracket.

But your approach reverses the mapping:

```python
brackets = {
    '(' : ')',
    '{' : '}',
    '[' : ']'
}
```

So when we encounter an opening bracket, we immediately store what we're going to need later.

For example:

```text
Input:
({[

Expected:
)]}
```

More precisely, the stack represents the expected closing brackets in the order they must occur:

```text
Opening brackets encountered:
(  {  [

Expected closing order:
)  }  ]
```

Because of the stack:

```text
stack = [')', '}', ']']
```

we naturally check:

```text
] → } → )
```

which is exactly the required closing order.

This makes the implementation particularly clean.

---

# 16. Time complexity

Let:

```text
n = len(s)
```

We iterate through the string exactly once:

```python
for ch in s:
```

Every character is pushed onto or popped from the stack at most once.

Therefore:

### Time

```text
O(n)
```

There is no nested loop and no repeated scanning of the string.

### Space

In the worst case, the string contains only opening brackets:

```text
(((((((((
```

Then every character gets stored in the stack.

Therefore:

```text
O(n)
```

space.

So the overall complexity is:

```text
Time:  O(n)
Space: O(n)
```

---

# 17. One small Python detail

This:

```python
elif ch in brackets:
```

is technically redundant.

You already have:

```python
if ch not in brackets:
```

If that condition is false, then `ch` **must** be in `brackets`.

Therefore, you could write:

```python
if ch not in brackets:
    ...
else:
    stack.append(brackets[ch])
```

So the code can be slightly simplified to:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for ch in s:
            if ch not in brackets:
                if not stack:
                    return False

                if stack.pop() != ch:
                    return False
            else:
                stack.append(brackets[ch])

        return not stack
```

The logic is exactly the same.

---

# 18. The core idea in one sentence

The entire solution can essentially be understood as:

> **For every opening bracket, push the closing bracket we expect; for every closing bracket, make sure it matches the most recently expected bracket.**

Or visually:

```text
Opening bracket
      │
      ▼
Find its matching close
      │
      ▼
Push it onto stack
      │
      ▼
Next closing bracket
      │
      ▼
Compare with stack.pop()
      │
   ┌──┴──┐
 match  mismatch
   │       │
   ▼       ▼
continue  False
```

And after the loop:

```text
stack empty?
   │
 ┌─┴─┐
Yes  No
 │    │
 ▼    ▼
True False
```

That is the whole algorithm: **the stack enforces the "last opened, first closed" rule that nested brackets require.**