from collections import deque

def dfs(graph, start, goal):
    """
    A function for depth-first search (DFS) in a graph.
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))
    return None

def bfs(graph, start, goal):
    """
    A function for breadth-first search (BFS) in a graph.
    """
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return None
