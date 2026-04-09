from prototype.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from prototype.Service_Layer.level_to_graph import level_to_graph
import math

level = 1

graph = level_to_graph(level)
print("Graph size: ", int(math.sqrt(graph.size)), "x", int(math.sqrt(graph.size)))
print("Graph after creation: ", graph.adj_matrix)

adjacent_matrix = prims_algorithm(graph)
graph.adj_matrix = adjacent_matrix
print("Graph after prim's algorithm: ", graph.adj_matrix)
