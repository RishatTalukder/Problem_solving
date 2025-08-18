queue = [0]
queue.append(1)
queue.append(36)
queue.append(2)
print(queue)


from collections import deque

st = deque(queue)
print(st)
st.append(102)
print(st)

popped = st.pop()
print(st)
print(popped)
popped_left = st.popleft()
print(st)
print(popped_left) 