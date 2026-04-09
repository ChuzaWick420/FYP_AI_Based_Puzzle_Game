# MST to grid
def mst_to_presentation_grid(graph):
    # NOTE: Nodes + Edges
    nodes_amount = graph.width
    edges_amount = graph.width - 1
    padding = 1 + 1
    grid_width = nodes_amount + edges_amount + padding

    presentation_grid = [[0] * grid_width for _ in range(grid_width)]

    # NOTE: Goes through padding (up and down)
    for i in range(0, grid_width):
        presentation_grid[0][i] = 0
        presentation_grid[grid_width - 1][i] = 0

    # NOTE: Goes through padding (right and left)
    for i in range(0, grid_width):
        presentation_grid[i][0] = 0
        presentation_grid[i][grid_width - 1] = 0

    # TODO: Create openings within padding
    presentation_grid[1][0] = 1
    presentation_grid[grid_width - 2][grid_width - 1] = 1

    offsets = (1, 1)

    # NOTE: Goes through each vertex
    for node_index in range(0, graph.total_nodes):

        (x, y) = graph.index_to_coordinates(node_index)

        up_allowed    = y - 1 >= 0          and graph.adj_matrix[node_index][graph.coordinates_to_index(x, y - 1)] != 0
        down_allowed  = y + 1 < graph.width and graph.adj_matrix[node_index][graph.coordinates_to_index(x, y + 1)] != 0
        right_allowed = x + 1 < graph.width and graph.adj_matrix[node_index][graph.coordinates_to_index(x + 1, y)] != 0
        left_allowed  = x - 1 >= 0          and graph.adj_matrix[node_index][graph.coordinates_to_index(x - 1, y)] != 0

        if (up_allowed):    presentation_grid[(y * 2) - 1 + offsets[1]][x * 2 + offsets[0]] = 1 
        if (down_allowed):  presentation_grid[(y * 2) + 1 + offsets[1]][x * 2 + offsets[0]] = 1 
        if (right_allowed): presentation_grid[y * 2 + offsets[0]][(x * 2) + 1 + offsets[0]] = 1 
        if (left_allowed):  presentation_grid[y * 2 + offsets[0]][(x * 2) - 1 + offsets[0]] = 1 

        # NOTE: Vertices
        presentation_grid[y * 2 + offsets[1]][x * 2 + offsets[0]] = 1

    return presentation_grid
