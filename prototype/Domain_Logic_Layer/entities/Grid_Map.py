from prototype.Data_Layer.CellTypes import CellTypes


class Grid_Map:
    def __init__(self, graph):

        # NOTE: Nodes + Edges
        nodes_amount = graph.width
        edges_amount = graph.width - 1
        padding = 1 + 1
        grid_width = nodes_amount + edges_amount + padding

        self.map = [[0] * grid_width for _ in range(grid_width)]

        # NOTE: Goes through padding (up and down)
        for i in range(0, grid_width):
            self.map[0][i] = CellTypes.WALL.value
            self.map[grid_width - 1][i] = CellTypes.WALL.value

        # NOTE: Goes through padding (right and left)
        for i in range(0, grid_width):
            self.map[i][0] = CellTypes.WALL.value
            self.map[i][grid_width - 1] = CellTypes.WALL.value

        # NOTE: Create openings within padding
        self.map[1][0] = CellTypes.PATH.value
        self.map[grid_width - 2][grid_width - 1] = CellTypes.PATH.value

        offsets = (1, 1)

        # NOTE: Goes through each vertex
        for node_index in range(0, graph.total_nodes):

            (x, y) = graph.index_to_coordinates(node_index)

            up_allowed    = y - 1 >= 0          and graph.adj_matrix[node_index][graph.coordinates_to_index(x, y - 1)] != 0
            down_allowed  = y + 1 < graph.width and graph.adj_matrix[node_index][graph.coordinates_to_index(x, y + 1)] != 0
            right_allowed = x + 1 < graph.width and graph.adj_matrix[node_index][graph.coordinates_to_index(x + 1, y)] != 0
            left_allowed  = x - 1 >= 0          and graph.adj_matrix[node_index][graph.coordinates_to_index(x - 1, y)] != 0

            if (up_allowed):    self.map[(y * 2) - 1 + offsets[1]][x * 2 + offsets[0]] = CellTypes.PATH.value
            if (down_allowed):  self.map[(y * 2) + 1 + offsets[1]][x * 2 + offsets[0]] = CellTypes.PATH.value
            if (right_allowed): self.map[y * 2 + offsets[0]][(x * 2) + 1 + offsets[0]] = CellTypes.PATH.value
            if (left_allowed):  self.map[y * 2 + offsets[0]][(x * 2) - 1 + offsets[0]] = CellTypes.PATH.value

            # NOTE: Vertices
            self.map[y * 2 + offsets[1]][x * 2 + offsets[0]] = CellTypes.PATH.value

    def get_map(self):
        return self.map
