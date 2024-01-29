import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import graph_algorithms as ga

# Setting a seed to generate a random graph
seed = 25

# Creating a graph
G = nx.erdos_renyi_graph(n=37, p=0.2, seed=seed)  # A random Erdos-Renyi graph with 37 vertices and a connection probability of 0.2

# Number of vertices and edges in the graph
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

# Calculating the average degree of vertices
average_degree = np.mean([degree for node, degree in G.degree()])

# Graph visualization
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=700, edge_color='gray')
plt.title("Homework 6 - Task 1 | Visualization of the corporate network topology")

# Add text with graph characteristics
text_str = f"Number of nodes: {num_nodes}\nNumber of edges: {num_edges}\nAverage degree: {average_degree:.2f}"
plt.figtext(0.5, 0.05, text_str, ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
plt.show()
