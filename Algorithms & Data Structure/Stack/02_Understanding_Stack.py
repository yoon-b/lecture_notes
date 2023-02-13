# <Using list>
stack1 = []

# append() to push element in the stack
stack1.append['a']
stack1.append['b']

# pop() to pop element from stack in LIFO order
print('\nElements popped from stack:')
print(stack1.pop())  # b
print(stack1.pop())

# <Using collections.deque>
# Use append() and pop() to push and pop element
from collections import deque
stack2 = deque()

stack2.append('a')
stack2.append('b')

print(stack2.pop())  # b

# <Using queue module>
from queue import LifoQueue

# Initializing a stack
# maxsize: # of items allowed in the queue
stack3 = LifoQueue(maxsize=3)

# Use put() and get() to push and pop element
stack3.put('a')
stack3.put('b')

print(stack3.get())  # b
