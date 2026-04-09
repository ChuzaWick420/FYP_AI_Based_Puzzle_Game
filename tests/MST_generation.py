from prototype.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from prototype.Domain_Logic_Layer.entities.Graph import Graph

size = 2 * 2

g = Graph(size)
# Debug
print("Graph after Creation", g.adj_matrix)

adjacent_matrix = prims_algorithm(g)
g.adj_matrix = adjacent_matrix

# Debug
print("Graph after Algorithm", g.adj_matrix)

