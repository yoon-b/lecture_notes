"""
from Los Angeles
to (possible destinations) Chicago, France, Ireland, Italy, Korea, New Delhi, Norway

LEVEL 0 begins
level = 0, queue = [A, None]
level = 0, pop, A, push, B, C, queue = [None, B, C]
pop None
→ queue = [B, C]

LEVEL 1 begins
push None
level = 1, queue = [B, C, None]
level = 1, pop, B, push, C, D, F, queue = [C, None, C, D, F]
level = 1, pop, C, push, D, D (lol!), queue = [None, C, D, F, D, D]
pop None 
→ queue = [C, D, F, D, D]

LEVEL 2 begins
push None
level = 2, queue = [C, D, F, D, D, None] .... and so on
"""

"""
# Using queue's size instead of None

queue = Queue()
queue.push(S)
level = 0
while queue is not empty:
    size = queue.size()  # size represents the number of elements in the current level      
    for i in 1..size:
        element = queue.pop()  # Process element here
        pass  # Perform a series of queue.push() operations here
    level += 1
"""
"""
<pseudo-code for the algorithm (Leetcode 787)>
def bfs(source, destination, K):  # K: (max. # of tolerable transfer) + 2 → max. airports visit for a route
    min_cost = {}  # representing min cost under K stops for each node reachable from source.
    set min_cost of source to be 0
    Q = [source]
    stops = 0
    while Q:
        size = len(Q)
        for i in range(size):
            element = Q.pop(0)
            if element == destination:
                continue
            for neighbor in adjacency list of element:
                if stops == K and neighbor != destination:
                    continue
                if min_cost of neighbor improves:
                    update and add back to the queue.
                    stops += 1

# No need to update the minimum cost if we have already exhausted our K stops. 
# if stops == K and neighbor != dst:    
#   continue
"""
"""
# 787. Cheapest Flights Within K Stops
# flights = [from, to, price]

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
adjLst = [[] for _ in range(3)]
for flight in flights:
    adjLst[flight[0]].append((flight[1], flight[2]))


minCost = {'0': 0}
queue = [src]
transfer = 0
while queue:
    size = len(queue)
    for i in range(size):
        stop = queue.pop()
        if stop == dst:
            continue
        for neighbor in adjLst:
            
"""