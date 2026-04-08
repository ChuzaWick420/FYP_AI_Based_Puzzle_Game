# Implementation Source: https://www.w3schools.com/dsa/dsa_algo_mst_prim.php

import random
import math

def getRandom():
    max = 9
    min = 1
    weight = min + int(random.random() * 10) % (max - min + 1)
    return weight

class Graph:
    def __init__(self, size):
        # NOTE: size is 2D (s = l * l)
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        self.initialize()

    def add_edge(self, u, v, weight): 
        # WARNING: If a request to overwrite an edge is made, it will be carried out.
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def index_1d_to_2d(self, index, width):
        # WARNING: 
        # Assumption:
        # index starts from 0 and first row and column are 0, not 1
        y = index // width
        x = index % width 
        return x, y

    def index_2d_to_1d(self, x, y, size):
        return y * size + x

    def initialize(self):
        one_dimensional_size = int(math.sqrt(self.size))

        for i in range(0, self.size):
            self.add_vertex_data(i, i)

        for i in range(0, self.size):
            # left_boundary =  int((i % one_dimensional_size)) == 0
            # right_boundary = int((i + 1) % one_dimensional_size) == 0
            # upper_boundary = int((i / one_dimensional_size)) < 1
            # lower_boundary = int((i / one_dimensional_size) + 1) == one_dimensional_size

            coords = self.index_1d_to_2d(i, one_dimensional_size)

            x = coords[0]
            y = coords[1]

            left_boundary =  x - 1 < 0
            right_boundary = x + 1 >= one_dimensional_size
            upper_boundary = y - 1 < 0
            lower_boundary = y + 1 >= one_dimensional_size

            if (not left_boundary):
                self.add_edge(i, self.index_2d_to_1d(x - 1, y, self.size), getRandom())
            if (not right_boundary):
                self.add_edge(i, self.index_2d_to_1d(x + 1, y, self.size), getRandom())
            if (not upper_boundary):
                self.add_edge(i, self.index_2d_to_1d(x, y - 1, self.size), getRandom())
            if (not lower_boundary):
                self.add_edge(i, self.index_2d_to_1d(x, y + 1, self.size), getRandom())
