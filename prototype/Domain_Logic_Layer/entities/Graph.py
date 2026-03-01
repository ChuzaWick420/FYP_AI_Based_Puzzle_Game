# Implementation Source: https://www.w3schools.com/dsa/dsa_algo_mst_prim.php

class Graph:
    def __init__(self, size):
        # NOTE: size is 2D (s = l * l)
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight): 
        # WARNING: If a request to overwrite an edge is made, it will be carried out.
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
