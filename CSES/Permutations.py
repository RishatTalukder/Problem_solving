# unclean version

n = int(input())

if n <= 3 and n > 1:
    print("NO SOLUTION")
    exit()

if n == 1:
    print(1)
    exit()

res = list(range(1, n+1, 2))

res2 = list(range(2, n+1, 2))

print(*(res2 + res if abs(res2[-1] - res[0]) != 1 else res[::-1] ))


# clean version
n = int(input())

# Special cases
if n == 1:
    print(1)
    exit()

if n <= 3:
    print("NO SOLUTION")
    exit()

# Build even and odd lists
evens = list(range(2, n + 1, 2))
odds = list(range(1, n + 1, 2))

# Try normal arrangement
result = evens + odds

# Check if it accidentally creates invalid adjacency
if abs(evens[-1] - odds[0]) == 1:
    result = odds[::-1] + evens

print(*result)