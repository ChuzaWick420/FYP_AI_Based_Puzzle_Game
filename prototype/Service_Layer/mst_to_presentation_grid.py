# MST to grid
def mst_to_presentation_grid(graph):
    # NOTE: Nodes + Edges
    grid_width = (graph.width) + (graph.width - 1) 
    presentation_grid = [[0] * grid_width for _ in range(grid_width)]

    # NOTE: Goes through each vertex
    for node_index in range(0, graph.total_nodes):

        (x, y) = graph.index_to_coordinates(node_index)

        up_allowed    = y - 1 >= 0          and graph.adj_matrix[node_index][graph.coordinates_to_index(x, y - 1)] != 0
        down_allowed  = y + 1 < graph.width and graph.adj_matrix[node_index][graph.coordinates_to_index(x, y + 1)] != 0
        right_allowed = x + 1 < graph.width and graph.adj_matrix[node_index][graph.coordinates_to_index(x + 1, y)] != 0
        left_allowed  = x - 1 >= 0          and graph.adj_matrix[node_index][graph.coordinates_to_index(x - 1, y)] != 0

        if (up_allowed):    presentation_grid[(y * 2) - 1][x * 2] = 1 
        if (down_allowed):  presentation_grid[(y * 2) + 1][x * 2] = 1 
        if (right_allowed): presentation_grid[y * 2][(x * 2) + 1] = 1 
        if (left_allowed):  presentation_grid[y * 2][(x * 2) - 1] = 1 

        # NOTE: Vertices
        presentation_grid[y * 2][x * 2] = 1

    return presentation_grid
