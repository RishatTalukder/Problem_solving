class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
            
            if key not in self.store:
                return ""
            
            arr = self.store[key]

            left = 0
            right = len(arr)-1

            while left <= right:
                mid = (left + right) >> 1

                print(left,mid,right)

                if arr[mid][1]  == timestamp:
                    return arr[mid][0]

                if arr[mid][1] <= timestamp:
                    left = mid + 1

                else:
                    right = mid - 1


            if right < 0:
                return ""
            
            return arr[right][0]


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
    
# pair = TimeMap()

# pair.set("foo", "bar", 1)

# print(pair.get("foo", 1))



# pair.set("foo", "bar2", 4)

# print(pair.get("foo", 3))