
def permutation(n):

    res = []

    array = []
    visited = set()

    def search():
        if len(array) == n:
            res.append(array.copy())
            return 


        for i in range(n):
            if i in visited:
                continue

            visited.add(i)

            array.append(i)

            search()

            array.pop()

            visited.remove(i)

    search()

    return res


print(permutation(3))