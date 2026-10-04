def subsets(n):
    subset = []

    result = []

    def search(k):
        if k == n:
            result.append(subset.copy())
            return 

        search(k+1)
        subset.append(k)
        search(k+1)
        subset.pop()

    search(0)

    return result


print(subsets(3))


def subsets_bitmask(n):
    res = []

    for bit in range(1<<n):
        subset = []

        for i in range(n):
            if (bit&(1<<i)):
                subset.append(i)

        res.append(subset)

    return res

print(subsets_bitmask(3))