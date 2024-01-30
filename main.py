import os
import sys
import random
import numpy as np
import networkx as nx
import graph_algorithms as ga
import matplotlib.pyplot as plt

# Create a random Erdos-Renyi graph with {nodes} nodes and a connection probability of {probability}
def create_random_graph(nodes, probability, seed):
    # Creating a graph
    G = nx.erdos_renyi_graph(n=nodes, p=probability, seed=seed)

    # Adding weights to graph edges
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)  # Weights from 1 to 10

    # Number of vertices and edges in the graph
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

    # Calculating the average degree of nodes
    average_degree = np.mean([degree for node, degree in G.degree()])
    return G, num_nodes, num_edges, average_degree

# Finding paths in a graph using DFS and BFS algorithms
def find_path_in_graph(G, start_node, goal_node):
    dfs_path = ga.dfs(G, start_node, goal_node)
    bfs_path = ga.bfs(G, start_node, goal_node)

    return dfs_path, bfs_path

# Graph visualization
def graph_visualization(G, num_nodes, num_edges, average_degree):
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightgreen', node_size=700, edge_color='gray')

    # Add edge weights as labels to a graph
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Add title
    plt.title("Homework 6 - Task 1 | Visualization of the corporate network topology")

    # Add text with graph characteristics
    text_str = f"Number of nodes: {num_nodes}\nNumber of edges: {num_edges}\nAverage degree: {average_degree:.2f}"
    plt.figtext(0.5, 0.05, text_str, ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
    plt.show()

# Main function
def main():
    # Setting parameters for generating a random graph
    nodes = 15         # Number of nodes
    probability = 0.2  # Probability
    seed = 25          # Seed

    start_node, goal_node = 0, 14 # Start node, goal node

    graph, num_nodes, num_edges, average_degree = create_random_graph(nodes, probability, seed)

    # Print the values of num_nodes, num_edges and average_degree
    print(f"Homework 6 - Task 1 | Number of nodes: {num_nodes}")
    print(f"Homework 6 - Task 1 | Number of edges: {num_edges}")
    print(f"Homework 6 - Task 1 | Average degree: {average_degree:.2f}")

    dfs_path, bfs_path = find_path_in_graph(graph, start_node, goal_node)

    # Print the values of dfs_path, bfs_path, start_node, goal_node
    print(f"Homework 6 - Task 2 | Start node: {start_node}")
    print(f"Homework 6 - Task 2 | Goal node: {goal_node}")
    print(f"Homework 6 - Task 2 | DFS path: {dfs_path}")
    print(f"Homework 6 - Task 2 | BFS path: {bfs_path}")

    # Print the values of Dijkstra shortest paths from {start_node} to {goal_node}
    for i in range(start_node, goal_node):
        shortest_path = ga.dijkstra_path(graph, start_node, i)
        print(f"Homework 6 - Task 3 | Dijkstra shortest path: {start_node} -> {i} == {shortest_path}")

    # Visualization of grap
    graph_visualization(graph, num_nodes, num_edges, average_degree)


# Launch the main function
if __name__ == "__main__":
    try:
        print(f"Homework 6 | Starting...")
        main()
        print(f"Homework 6 | Done")
    except KeyboardInterrupt:
        print(f"\nHomework 6 | Good bye!")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
