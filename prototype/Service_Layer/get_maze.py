from prototype.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from prototype.Domain_Logic_Layer.entities.Graph import Graph
from prototype.Service_Layer.maze_generator import visualize_grid
from prototype.Service_Layer.mst_to_presentation_grid import mst_to_presentation_grid


def get_presentation_grid(size):
    graph = Graph(size)
    mst = prims_algorithm(graph)
    graph.adj_matrix = mst
    grid = mst_to_presentation_grid(graph)

    return grid
