# Count Ways to Build the Same Binary Search Tree Using Combinatorics and Recursion

## Intuition

The key to this problem is understanding **what determines the structure of a Binary Search Tree (BST)**.

When we insert numbers into a BST, the first number becomes the root. Every smaller number goes into the left subtree, and every larger number goes into the right subtree.

For example, consider this insertion order:

`[3, 1, 5, 2, 4]`

The resulting BST looks like this:

```text
        3
       / \
      1   5
       \  /
        2 4
```

Now, suppose we want to find other insertion orders that produce exactly the same BST.

We cannot simply rearrange the numbers however we like. The root must remain `3`, because the first inserted number always becomes the root. Also, `1` and `2` must remain in the left subtree, while `4` and `5` must remain in the right subtree.

However, **the relative order of elements belonging to different subtrees can change without changing the final BST**.

For example, consider these two insertion orders:

```text
[3, 1, 5, 2, 4]
[3, 5, 1, 4, 2]
```

Both produce the same BST.

Why? After inserting `3`, the elements `1` and `2` build the left subtree, while `4` and `5` build the right subtree. The elements from the two sides can be interleaved in different ways, as long as the relative order within each side stays the same.

This gives us our first major observation:

**Once the root is fixed, we can independently arrange the left and right subtrees, then interleave their insertion sequences in different ways.**

The challenge is counting all those possibilities without generating them individually.

## The Mathematics Behind the Solution

### 1. The root divides the problem into two smaller problems

Let the original sequence contain \(n\) distinct numbers, and let its first element be the root.

Because of the BST property, every remaining element belongs to exactly one of two groups:

- \(L\): elements smaller than the root, which form the left subtree.
- \(R\): elements larger than the root, which form the right subtree.

Let

\[
\ell = |L|,\qquad r = |R|
\]

Then:

\[
\ell+r=n-1
\]

The root is fixed at the beginning. After that, we need to determine how the elements of \(L\) and \(R\) can be arranged while preserving the same tree.

Suppose there are:

- \(W(L)\) insertion orders that produce the required left subtree.
- \(W(R)\) insertion orders that produce the required right subtree.

If we know these two quantities, we can use them to count the possible insertion orders for the entire tree.

This is the recursive structure of the problem.

### 2. Why must the relative order within each subtree stay the same?

Imagine that the left subtree has the elements:

```text
L = [1, 2, 4]
```

Suppose this is the insertion order of those elements in the original sequence.

We cannot arbitrarily change it to `[2, 1, 4]` if that would produce a different left subtree.

However, we can insert elements from the right subtree between them.

For example:

```text
Left-subtree order:  1, 2, 4
Right-subtree order: 3, 5
```

The following interleavings preserve both relative orders:

```text
1, 3, 2, 5, 4
3, 1, 2, 4, 5
1, 2, 3, 4, 5
```

Notice that the elements belonging to the left subtree never change their relative order, and neither do the elements belonging to the right subtree.

This restriction is important. We are not freely permuting all \(n-1\) elements. We are **merging two sequences while preserving the order of each sequence**.

That is precisely where combinatorics comes in.

### 3. Deriving the binomial coefficient

After fixing the root, we have \(n-1\) remaining positions.

Out of those positions:

- Exactly \(\ell\) must be occupied by elements from the left subtree.
- Exactly \(r\) must be occupied by elements from the right subtree.

The question becomes:

**In how many ways can we choose the positions occupied by the left-subtree elements?**

We need to select \(\ell\) positions from \(n-1\) available positions. The number of ways to do this is the binomial coefficient:

\[
\binom{n-1}{\ell}
=
\frac{(n-1)!}{\ell!(n-1-\ell)!}
\]

Since \(n-1-\ell=r\), we can also write:

\[
\binom{n-1}{\ell}
=
\frac{(n-1)!}{\ell!r!}
\]

Once we choose those positions, the remaining positions automatically belong to the right subtree.

For every such choice, we can place a valid left-subtree insertion order in the selected positions and a valid right-subtree insertion order in the remaining positions.

Therefore, the total number of ways to interleave the two subtrees is:

\[
\binom{n-1}{\ell}W(L)W(R)
\]

This is the central mathematical formula behind the solution.

The three factors have distinct meanings:

- \(W(L)\): choose a valid insertion order for the left subtree.
- \(W(R)\): choose a valid insertion order for the right subtree.
- \(\binom{n-1}{\ell}\): choose how to interleave the two orders.

Multiplying them works because these are independent choices.

Thus, if \(W(T)\) represents the number of insertion orders producing the same BST \(T\), we obtain:

\[
\boxed{
W(T)=
\binom{n-1}{\ell}W(L)W(R)
}
\]

### 4. A complete numerical example

Consider the sequence:

```text
nums = [3, 1, 5, 2, 4]
```

Its BST has root `3`.

The left subtree contains `[1, 2]`, while the right subtree contains `[5, 4]`.

Therefore:

\[
n=5,\qquad \ell=2,\qquad r=2
\]

The number of ways to interleave the left and right subtree elements is:

\[
\binom{4}{2}
=
\frac{4!}{2!2!}
=
6
\]

There are six possible patterns indicating which of the four positions belong to the left subtree:

```text
LLRR
LRLR
LRRL
RLLR
RLRL
RRLL
```

Here, `L` means the next element comes from the left-subtree sequence, and `R` means it comes from the right-subtree sequence.

For this example, both subtrees contain two nodes, and each subtree has exactly one valid insertion order that produces its required shape. Consequently:

\[
W(L)=1,\qquad W(R)=1
\]

The total number of insertion orders that produce the same BST is therefore:

\[
W(T)=6\cdot1\cdot1=6
\]

One of these six orders is the original sequence itself.

Since the problem asks for the number of *other* insertion orders, we subtract one:

\[
\boxed{\text{Answer}=6-1=5}
\]

This explains why the final result subtracts one from the total number of valid insertion orders.

### 5. Why does the formula work recursively?

The left and right subtrees are themselves BSTs created by inserting their respective elements in some order.

To reproduce the original tree, we must preserve the required structure of each subtree. But we can choose any valid insertion order that creates that same subtree.

This means that counting the possible insertion orders for the entire tree depends on counting the possible insertion orders for its two smaller subtrees.

The same reasoning applies to each subtree:

\[
W(L)=
\binom{\ell-1}{\ell_L}
W(L_L)W(L_R)
\]

and

\[
W(R)=
\binom{r-1}{r_L}
W(R_L)W(R_R)
\]

Here, \(L_L\) and \(L_R\) denote the left and right subtrees of the root of \(L\), and \(R_L\) and \(R_R\) denote those of \(R\). The quantities \(\ell_L\) and \(r_L\) are the sizes of the corresponding left subtrees.

Rather than writing a separate formula for every possible tree, we apply the same rule at every node.

Eventually, we reach subtrees with fewer than three nodes. For these cases, there is exactly one valid insertion order for the given subtree:

\[
W(T)=1\qquad\text{when }|T|<3
\]

A subtree with one or two distinct nodes has only one possible insertion order that creates its particular BST shape.

This is the base case that terminates the recursion.

### 6. Why do we use modulo arithmetic?

The number of valid insertion orders can grow very quickly as the tree gets larger. We therefore calculate the answer modulo:

\[
M=10^9+7
\]

The recurrence becomes:

\[
W(T)=
\left[
\binom{n-1}{\ell}W(L)W(R)
\right]\bmod M
\]

Modulo arithmetic allows us to keep the intermediate results bounded without changing the final answer modulo \(M\).

The binomial coefficient is calculated using `comb`, which returns the exact integer binomial coefficient. The multiplication is then reduced modulo \(M\).

Finally, because the original insertion sequence is included among the valid orders, the answer to the problem is:

\[
\boxed{(W(T)-1)\bmod M}
\]

The final modulo operation also ensures the result is nonnegative if the count is congruent to zero modulo \(M\).

## Approach

1. Treat the first number as the root of the BST.
2. Partition the remaining numbers into those smaller than the root and those larger than the root.
3. Recursively count the valid insertion orders for the left and right subtrees.
4. Use the binomial coefficient \(\binom{n-1}{|L|}\) to count the ways of interleaving their insertion sequences while preserving their internal relative orders.
5. Multiply the three quantities and take the result modulo \(10^9+7\).
6. Subtract one to exclude the original insertion order.

## Complexity

Let \(n\) be the number of elements.

- **Time complexity:** The recursive partitioning takes \(O(n^2)\) time in the worst case, when the BST is highly unbalanced. Each recursive call scans the elements to construct its left and right subtrees.
- **Space complexity:** \(O(n^2)\) in the worst case when accounting for the cumulative storage of newly created subtree lists across recursive calls. The recursion stack itself can reach \(O(n)\) depth.

## Code

```python
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def dp(nums):
            m = len(nums)

            if m < 3:
                return 1

            left = [num for num in nums if num < nums[0]]
            right = [num for num in nums if num > nums[0]]

            return (
                dp(left) * dp(right) * comb(m - 1, len(left))
            ) % MOD

        return (dp(nums) - 1) % MOD
```