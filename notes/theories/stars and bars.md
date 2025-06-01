# 🌟 Stars and Bars Theorem

The **Stars and Bars** theorem is a classic combinatorial method used to count the number of **non-negative** or **positive** integer solutions to equations of the form:

```
x₁ + x₂ + ... + xₖ = n
```

This technique is especially useful in problems of distributing **identical items** (stars) among **distinct groups** (bins or bars).

---

## 🧮 Case 1: Non-negative integer solutions (xᵢ ≥ 0)

We want to find the number of ways to distribute `n` identical items among `k` distinct bins, where **each bin can hold 0 or more items**.

This is equivalent to placing `k - 1` dividers (bars) between the `n` stars.

**Number of ways:**

$$
\binom{n + k - 1}{k - 1}
$$

---

## ➕ Example:

Distribute 5 candies among 3 children (candies are identical, children are distinct):

$$
\binom{5 + 3 - 1}{3 - 1} = \binom{7}{2} = 21
$$

---

## 🧮 Case 2: Positive integer solutions (xᵢ ≥ 1)

Here, each bin must receive **at least one item**.

To ensure this, give each bin one item first. Now you’re left with `n - k` items to distribute freely (allowing 0 now is okay).

**Number of ways:**

$$
\binom{n - 1}{k - 1}
$$

---

## ➕ Example:

Distribute 5 candies among 3 children such that each child gets **at least one** candy:

$$
\binom{5 - 1}{3 - 1} = \binom{4}{2} = 6
$$

---

## 🧠 Why It Works

The key idea is to convert the problem of solving an equation into placing dividers among identical objects. Each **star** represents an item, and each **bar** separates a group (or person). The total number of placements of stars and bars determines the number of solutions.

---

## 📦 Applications

* Distributing candies among children
* Integer partition problems
* Combinatorial proofs
* Probability distributions

---

Let me know if you want a visual diagram version of this or an example in code!

## Related Problems

* [[2929 Distribute Candies Among Children]]