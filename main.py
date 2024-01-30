import os
import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import graph_algorithms as ga

# Create a random Erdos-Renyi graph with {nodes} nodes and a connection probability of {probability}
def create_random_graph(nodes, probability, seed):
    # Creating a graph
    G = nx.erdos_renyi_graph(n=nodes, p=probability, seed=seed)

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
    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color='lightgreen', node_size=700, edge_color='gray')
    plt.title("Homework 6 - Task 1 | Visualization of the corporate network topology")

    # Add text with graph characteristics
    text_str = f"Number of nodes: {num_nodes}\nNumber of edges: {num_edges}\nAverage degree: {average_degree:.2f}"
    plt.figtext(0.5, 0.05, text_str, ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
    plt.show()

def main():
    # Setting parameters for generating a random graph
    nodes=15         # Number of nodes
    probability=0.2  # Probability
    seed = 25        # Seed

    start_node, goal_node = 0, 14

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

    graph_visualization(graph, num_nodes, num_edges, average_degree)

if __name__ == "__main__":
    try:
        print(f"Homework 6 | Starting...")
        main()
    except KeyboardInterrupt:
        print(f"\nHomework 6 | Good bye!")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)