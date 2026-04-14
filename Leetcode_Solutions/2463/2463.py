from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        factory_positions = []
        for f in factory:
            for _ in range(f[1]):
                factory_positions.append(f[0])

        @lru_cache(None)
        def dp(i, j):
            if i == len(robot):
                return 0
            if j == len(factory_positions):
                return float("inf")

            assign = abs(robot[i] - factory_positions[j]) + dp(i + 1, j + 1)
            skip = dp(i, j + 1)

            return min(assign, skip)

        return dp(0, 0)