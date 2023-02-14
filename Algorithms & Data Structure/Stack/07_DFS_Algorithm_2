def dfs(graph, start, visited=None):
    if visited is None:  # initialize
        visited = set()
    visited.add(start)  # start vertex is always visited

    print(start)

    for next in graph[start] - visited:  # unvisted vertex in the adjacent 
        dfs(graph, next, visited)
    return visited

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')

