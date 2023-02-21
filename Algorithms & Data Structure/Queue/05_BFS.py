def bfs(graph, startNode):
    visitedNodes = []
    queue = [startNode]

    while queue:
        currentNode = queue.pop(0)
        visitedNodes.append(currentNode)
        for neighbor in graph[currentNode]:
            if neighbor not in visitedNodes:
                queue.append(neighbor)

    return visitedNodes


# Shortest Path Implementation
def bfsShortestPath(graph, startNode, endNode):
    visitedNodes = []
    queue = [startNode]
    predecessorNode = {}  # use this dictionary to backtrack to find the shortest path

    while queue:
        currentNode = queue.pop(0)
        visitedNodes.append(currentNode)
        for neighbor in graph[currentNode]:
            if neighbor not in visitedNodes:
                queue.append(neighbor)
                predecessorNode[neighbor] = currentNode

    print(predecessorNode)

    print(shortestPath(predecessorNode, startNode, endNode))
    return True


def shortestPath(predecessorNode, startNode, endNode):
    path = [endNode]
    currentNode = endNode
    while currentNode != startNode:
        currentNode = predecessorNode[currentNode]
        path.append(currentNode)
    path.reverse()
    return path


"""
# example
testGraph = {'0': ['3', '5', '9'],
             '1': ['6', '7', '4'],
             '2': ['10', '5'],
             '3': ['0'],
             '4': ['1', '5', '8'],
             '5': ['0', '2', '4'],
             '6': ['1'],
             '7': ['1'],
             '8': ['4'],
             '9': ['0'],
             '10': ['2']
             }

bfsShortestPath(testGraph, '0', '1')
"""
