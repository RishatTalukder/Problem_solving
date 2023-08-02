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



candies = [12,1,12]
extraCandies = 10

print(Solution().kidsWithCandies(candies,extraCandies))