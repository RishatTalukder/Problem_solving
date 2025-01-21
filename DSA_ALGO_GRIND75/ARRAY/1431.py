class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int):
        maximum = max(candies)

        bool_value = []
        for i in candies:
            if i+extraCandies >= maximum:
                bool_value.append(True)

            else:
                bool_value.append(False)

        return bool_value

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)

        for ind, candy in enumerate(candies):
            candies[ind] = candy+extraCandies >= greatest

        return candies

candies = [12,1,12]
extraCandies = 10

print(Solution().kidsWithCandies(candies,extraCandies))