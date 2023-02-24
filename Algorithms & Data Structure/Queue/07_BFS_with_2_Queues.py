# deque can be used for better performance, 
# meaning that it's faster and use lesser memory

def levelOrder(lst: list, s: int):  # lst: adjacent list
    if len(lst) == 0:
        return None
    
    queue = [s]  # s: starting index
    result = []  # storage for the final result
    visited = [0] * len(lst)

    while queue:
        level = []  # storage for each level's elements
        l = len(queue)  # to repeat for the length of current level's elements
        for i in range(l):
            current = queue.pop(0)
            level.append(current)
            
            if lst(current):
                for c in lst[current]:
                    if c not in visited:
                        queue.append(c)
        
        result.append(level)
    
    return result