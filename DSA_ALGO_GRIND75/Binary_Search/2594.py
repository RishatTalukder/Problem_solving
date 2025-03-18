class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = min(ranks)*(cars**2)

        def can_repair_cars(time):
            cars_repaired = 0
            for rank in ranks:
                cars_repaired += int((time/rank)**0.5)
            return cars_repaired >= cars
        
        while left < right:
            mid = (left + right) // 2
            if can_repair_cars(mid):
                right = mid
            else:
                left = mid + 1

        return left