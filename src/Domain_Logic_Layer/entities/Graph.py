# Implementation Source: https://www.w3schools.com/dsa/dsa_algo_mst_prim.php

import random
import math

class Graph:
    def __init__(self, num_of_nodes):
        self.__adj_matrix = [[0] * num_of_nodes for _ in range(num_of_nodes)]
        self.__total_nodes = num_of_nodes
        self.__width = int(math.sqrt(num_of_nodes))
        self.__vertex_data = [''] * num_of_nodes
        self.initialize()

    def add_edge(self, u, v, weight): 
        # WARNING: can be overwriten
        if 0 <= u < self.__total_nodes and 0 <= v < self.__total_nodes:
            self.__adj_matrix[u][v] = weight
            self.__adj_matrix[v][u] = weight  # NOTE: For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.__total_nodes:
            self.__vertex_data[vertex] = data

    def index_to_coordinates(self, index):
        y = index // self.__width # NOTE: Row number
        x = index % self.__width  # NOTE: Column number
        return x, y

    def coordinates_to_index(self, x, y):
        return y * self.__width + x

    def initialize(self):

        for i in range(0, self.__total_nodes):
            self.add_vertex_data(i, str(i))

            (x, y) = self.index_to_coordinates(i)

            # NOTE: Boundary checking before population
            left_violated  = x - 1 < 0
            right_violated = x + 1 >= self.__width
            up_violated    = y - 1 < 0
            down_violated  = y + 1 >= self.__width

            if (not left_violated):
                self.add_edge(i, self.coordinates_to_index(x - 1, y), random.randint(1, 9))
            if (not right_violated):
                self.add_edge(i, self.coordinates_to_index(x + 1, y), random.randint(1, 9))
            if (not up_violated):
                self.add_edge(i, self.coordinates_to_index(x, y - 1), random.randint(1, 9))
            if (not down_violated):
                self.add_edge(i, self.coordinates_to_index(x, y + 1), random.randint(1, 9))

    def getAdjMatrix(self):
        return self.__adj_matrix

    def setAdjMatrix(self, matrix):
        self.__adj_matrix = matrix

    def getNodesCount(self):
        return self.__total_nodes

    def setNodesCount(self, amount):
        self.__total_nodes = amount
        self.__width = int(math.sqrt(amount))

    def getWidth(self):
        return self.__width
