from collections import defaultdict
from heapq import heappush, heappop


class NumberContainers:

    def __init__(self):
        self.arr = defaultdict(int)
        self.val_map = defaultdict(list)
        

    def change(self, index: int, number: int) -> None:
        if index in self.arr:
            prev_num = self.arr[index]
            if prev_num == number:
                return
            self.val_map[self.arr[index]].remove(index)
            if not self.val_map[self.arr[index]]:
                del self.val_map[self.arr[index]]
        
        self.arr[index] = number
        heappush(self.val_map[number], index)


    def find(self, number: int) -> int:
        if number in self.val_map:
            return self.val_map[number][0]
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)