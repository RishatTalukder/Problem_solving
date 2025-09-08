from collections import deque

stack = deque([1,2,3,4,5])
print(stack) 
stack.append(123)
print(stack)
popped = stack.popleft()
print(stack)
print(f'popped: {popped}')