# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         minn = self.stack[0]
#         for i in self.stack:
#             if i < minn:
#                 minn = i

#         return minn
    


# # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(1)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# same class but faster
class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = float("inf")

    def push(self, val: int) -> None: 
        if val <= self.minn:
            self.stack.append(self.minn)
            self.minn = val
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minn:
            self.minn = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn
    
if __name__ == "__main__":
    obj = MinStack()
    obj.push(-1)
    print(obj.stack)
    obj.push(0)
    print(obj.stack)
    obj.push(-3)
    print(obj.stack)
    obj.pop()
    print(obj.stack)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)



class MinStack:

    def __init__(self):
        self.stack = []
        
        self.min = float('inf')
        self.min_stack = [self.min]

    def push(self, val: int) -> None:
        if val <= self.min:
            self.min_stack.append(val)
            self.min = val
        else:
            self.min_stack.append(self.min)

        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.min = self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min