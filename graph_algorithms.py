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

def dijkstra_path(graph, start, goal):
    """
    Dijkstra's algorithm for finding the shortest paths in the graph.
    """
    # Initialize shortcuts and preceding nodes
    shortest_paths = {vertex: float('infinity') for vertex in graph.nodes()}
    previous_nodes = {vertex: None for vertex in graph.nodes()}
    shortest_paths[start] = 0
    nodes = set(graph.nodes())

    while nodes:
        current_node = min(nodes, key=lambda vertex: shortest_paths[vertex])
        nodes.remove(current_node)

        if current_node == goal:
            break

        for neighbor, data in graph[current_node].items():
            weight = data['weight']
            distance = shortest_paths[current_node] + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                previous_nodes[neighbor] = current_node

    # Restoring the path
    path, current = [], goal
    while previous_nodes[current] is not None:
        path.insert(0, (previous_nodes[current], current, {'weight': graph[previous_nodes[current]][current]['weight']}))
        current = previous_nodes[current]

    return path if path else None
