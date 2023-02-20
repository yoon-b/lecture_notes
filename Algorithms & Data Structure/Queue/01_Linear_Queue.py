# Linear Queue

def enQueue(data):
    global rear
    rear += 1
    queue[rear] = data
    return queue

def deQueue():
    global front
    front += 1
    queue[front]
    return queue[front]

queue = [0] * 10
front = rear = -1


enQueue(1)
enQueue(2)
enQueue(3)

print(deQueue())  # 1
print(deQueue())  # 2

if front != rear:  # 3
    print(deQueue())

if front != rear:  # not executed
    print(deQueue())

"""
append w/ pop → Queue 활용 보다 느림

cf) from collections import deque
→ append w/ popleft: Queue와 속도 비슷
"""