class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empty = numBottles
        rate = numExchange

        while empty >= rate:
            empty = empty - rate + 1
            rate += 1
            drank += 1

        return drank