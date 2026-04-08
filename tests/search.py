from prototype.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from prototype.Domain_Logic_Layer.entities.Graph import Graph

import math

size = 3 * 3

graph = Graph(size)

# NOTE: Debug
print("Adjacent matrix after creation: ", graph.adj_matrix)

mst = prims_algorithm(graph)
graph.adj_matrix = mst

# NOTE: Debug
print("Adjacent matrix after prim's algorithm: ", graph.adj_matrix)

# MST to grid
def generateMSTGrid(g):
    size = int(math.sqrt(g.size))
    # TODO: Generate presentation grid
    grid_1d_size = (size) + (size - 1) # NOTE: Nodes + Edges
    grid = [[0] * grid_1d_size for _ in range(grid_1d_size)]

    # NOTE: Goes through each vertex, index starting at 0
    for node_index in range(0, g.size):
        coords = g.index_1d_to_2d(node_index, size)
        x = coords[0]
        y = coords[1]

        # TODO: Check up, down, right and left for the edges
        # NOTE: Edges
        # NOTE: UP
        if (y - 1 >= 0 and g.adj_matrix[node_index][g.index_2d_to_1d(x, y - 1, size)] != 0):
            grid[x * 2][(y * 2) - 1] = 1

        # NOTE: DOWN
        if (y + 1 < size and g.adj_matrix[node_index][g.index_2d_to_1d(x, y + 1, size)] != 0):
            grid[x * 2][(y * 2) + 1] = 1

        # NOTE: RIGHT
        if (x + 1 < size and g.adj_matrix[node_index][g.index_2d_to_1d(x + 1, y, size)] != 0):
            grid[(x * 2) + 1][y * 2] = 1

        # NOTE: LEFT
        if (x - 1 >= 0 and g.adj_matrix[node_index][g.index_2d_to_1d(x - 1, y, size)] != 0):
            grid[(x * 2) - 1][y * 2] = 1

        # NOTE: Vertices
        grid[x * 2][y * 2] = 1


    # DEBUG
    print("Presentation Grid: ", grid)

generateMSTGrid(graph)
