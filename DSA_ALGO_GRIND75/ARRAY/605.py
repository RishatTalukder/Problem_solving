# class Solution:
#     def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
#         possible_number_of_plant = -(-len(flowerbed)//2)
#         counter = 0
#         for i in flowerbed:
#             if i:
#                 counter += 1

#         if possible_number_of_plant - counter >= n:
#             return True 

#         else:
#             return False

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]  
        for i in range(1, len(flowerbed) - 1): 
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:  
                flowerbed[i] = 1  
                n -= 1 
            if n == 0:  
                return True 
        return n <= 0  

flowerbed = [0,1,0]
n = 1



class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
            
        return n <= 0