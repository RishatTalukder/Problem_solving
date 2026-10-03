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