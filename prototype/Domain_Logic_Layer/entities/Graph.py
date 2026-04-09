# Implementation Source: https://www.w3schools.com/dsa/dsa_algo_mst_prim.php

import random
import math

def get_random_int(min = 1, max = 9):
    weight = min + int(random.random() * 10) % (max - min + 1)
    return weight

class Graph:
    def __init__(self, num_of_nodes):
        self.adj_matrix = [[0] * num_of_nodes for _ in range(num_of_nodes)]
        self.total_nodes = num_of_nodes
        self.width = int(math.sqrt(num_of_nodes))
        self.vertex_data = [''] * num_of_nodes
        self.initialize()

    def add_edge(self, u, v, weight): 
        # WARNING: can be overwriten
        if 0 <= u < self.total_nodes and 0 <= v < self.total_nodes:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # NOTE: For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.total_nodes:
            self.vertex_data[vertex] = data

    def index_to_coordinates(self, index):
        y = index // self.width # NOTE: Row number
        x = index % self.width  # NOTE: Column number
        return x, y

    def coordinates_to_index(self, x, y):
        return y * self.width + x

    def initialize(self):

        for i in range(0, self.total_nodes):
            self.add_vertex_data(i, str(i))

            (x, y) = self.index_to_coordinates(i)

            # NOTE: Boundary checking before population
            left_violated =  x - 1 < 0
            right_violated = x + 1 >= self.width
            up_violated = y - 1 < 0
            down_violated = y + 1 >= self.width

            if (not left_violated):
                self.add_edge(i, self.coordinates_to_index(x - 1, y), get_random_int())
            if (not right_violated):
                self.add_edge(i, self.coordinates_to_index(x + 1, y), get_random_int())
            if (not up_violated):
                self.add_edge(i, self.coordinates_to_index(x, y - 1), get_random_int())
            if (not down_violated):
                self.add_edge(i, self.coordinates_to_index(x, y + 1), get_random_int())
