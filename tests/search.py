from prototype.Domain_Logic_Layer.algorithms.a_star_search_algo import a_star_search
from prototype.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from prototype.Domain_Logic_Layer.entities.Graph import Graph
from prototype.Service_Layer.mst_to_presentation_grid import mst_to_presentation_grid

size = 3 * 3

graph = Graph(size)

# NOTE: Debug
print("Adjacent matrix after creation: ", graph.adj_matrix)

mst = prims_algorithm(graph)
graph.adj_matrix = mst

# NOTE: Debug
print("Adjacent matrix after prim's algorithm: ", graph.adj_matrix)

grid = mst_to_presentation_grid(graph)

# NOTE: Debug
print("Presentation Grid: ", grid)

src = []
dest = []

a_star_search(grid, src, dest)
