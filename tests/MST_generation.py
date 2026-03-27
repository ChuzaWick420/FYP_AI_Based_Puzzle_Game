from prototype.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from prototype.Service_Layer.populate_graph import populate_graph
from prototype.Domain_Logic_Layer.entities.Graph import Graph

size = 2 * 2

g = Graph(size)
# Debug
print("Graph after Creation", g.adj_matrix)

populate_graph(g, size)
# Debug
print("Graph after Population", g.adj_matrix)

prims_algorithm(g)
# Debug
print("Graph after Algorithm", g.adj_matrix)

