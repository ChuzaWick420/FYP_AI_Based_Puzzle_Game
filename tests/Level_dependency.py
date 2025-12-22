from prototype.algorithms.prims_algo import prims_algorithm
from prototype.services.populate_graph import populate_graph
from prototype.services.level_to_graph import level_to_graph
import math

level = 1

graph = level_to_graph(level)
print("Graph size: ", int(math.sqrt(graph.size)), "x", int(math.sqrt(graph.size)))
print("Graph after creation: ", graph.adj_matrix)

populate_graph(graph, graph.size)
print("Graph after population: ", graph.adj_matrix)

prims_algorithm(graph)
print("Graph after prim's algorithm: ", graph.adj_matrix)
