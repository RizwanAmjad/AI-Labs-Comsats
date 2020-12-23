from _collections import deque

f = deque()
f.append(10)
f.append(8)
f.append(13)

print(f.pop())
print(f.popleft())