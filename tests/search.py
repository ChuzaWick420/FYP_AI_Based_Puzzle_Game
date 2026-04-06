from prototype.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from prototype.Domain_Logic_Layer.entities.Graph import Graph

import math

size = 9 * 9

graph = Graph(size)

mst = prims_algorithm(graph)
graph.adj_matrix = mst

# MST to grid
# FIXME: Implementation needs to be rethinked about
def generateMSTGrid(g):
    size = int(math.sqrt(g.size))
    grid = [[0] * size for _ in range(size)]

    for node_index in range(0, g.size):
        coords = g.index_1d_to_2d(node_index, size)
        x = coords[0]
        y = coords[1]

