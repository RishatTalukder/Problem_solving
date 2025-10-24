class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        i = n + 1

        while True:
            c = Counter(str(i))
            if all(c[d] == int(d) for d in c):
                return i

            i+=1