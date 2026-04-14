from prototype.Data_Layer import Global
from prototype.Data_Layer.CellColors import CellColors
from prototype.Data_Layer.CellTypes import CellTypes
from prototype.Domain_Logic_Layer.algorithms.a_star_search_algo import a_star_search
from prototype.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from prototype.Domain_Logic_Layer.entities.Graph import Graph


class Maze_Manager:
    def __init__(self):
        self.render_data = []
        pass

    def load_previous(self, level_number, previous_graph):
        size = (level_number * 3) ** 2
        self.graph = Graph(size)
        self.graph.adj_matrix = previous_graph
        self.maze_map = self.generate_grid_map()
        self.render_data = [((-1, -1, -1), (-1, -1), (-1, -1))] * (len(self.maze_map) ** 2)
        self.search()
        self.spawn_entities()
        self.initialize_render_data()

    def initialize(self, level_number):

        size = (level_number * 3) ** 2

        self.graph = Graph(size)
        mst = prims_algorithm(self.graph)
        self.graph.adj_matrix = mst
        self.maze_map = self.generate_grid_map()
        self.render_data = [((-1, -1, -1), (-1, -1), (-1, -1))] * (len(self.maze_map) ** 2)
        self.search()
        self.spawn_entities()
        self.initialize_render_data()

        # DEBUG:
        # print("Source: ", src)
        # print("Destination: ", dest)
        #
        # for row in self.maze_map:
        #     print(row)

    def search(self):

        # DEBUG:
        # print("Type: {0}, data: {1}".format(type(self.maze_map), self.maze_map))

        size = len(self.maze_map)

        print("size: ", size)

        # NOTE: Format: (y, x)
        src = [1, 0]
        dest = [size - 2, size - 1]

        # NOTE: Get the path before populating the grid
        self.path = a_star_search(self.maze_map, src, dest, size)

    def spawn_entities(self):
        # TODO: Spawn power ups

        # grid_width = len(grid)
        # for j in range(0, grid_width):
        #     for i in range(0, grid_width):
        #         if grid[j][i] == CellTypes.PATH:
        #

        self.maze_map[1][0] = CellTypes.PLAYER_AND_AI.value

    def generate_grid_map(self):
        # NOTE: Nodes + Edges
        nodes_amount = self.graph.width
        edges_amount = self.graph.width - 1
        padding = 1 + 1
        grid_width = nodes_amount + edges_amount + padding

        map = [[0] * grid_width for _ in range(grid_width)]

        # NOTE: Goes through padding (up and down)
        for i in range(0, grid_width):
            map[0][i] = CellTypes.WALL.value
            map[grid_width - 1][i] = CellTypes.WALL.value

        # NOTE: Goes through padding (right and left)
        for i in range(0, grid_width):
            map[i][0] = CellTypes.WALL.value
            map[i][grid_width - 1] = CellTypes.WALL.value

        # NOTE: Create openings within padding
        map[1][0] = CellTypes.PATH.value
        map[grid_width - 2][grid_width - 1] = CellTypes.PATH.value

        offsets = (1, 1)

        # NOTE: Goes through each vertex
        for node_index in range(0, self.graph.total_nodes):

            (x, y) = self.graph.index_to_coordinates(node_index)

            up_allowed    = y - 1 >= 0          and self.graph.adj_matrix[node_index][self.graph.coordinates_to_index(x, y - 1)] != 0
            down_allowed  = y + 1 < self.graph.width and self.graph.adj_matrix[node_index][self.graph.coordinates_to_index(x, y + 1)] != 0
            right_allowed = x + 1 < self.graph.width and self.graph.adj_matrix[node_index][self.graph.coordinates_to_index(x + 1, y)] != 0
            left_allowed  = x - 1 >= 0          and self.graph.adj_matrix[node_index][self.graph.coordinates_to_index(x - 1, y)] != 0

            if (up_allowed):    map[(y * 2) - 1 + offsets[1]][x * 2 + offsets[0]] = CellTypes.PATH.value
            if (down_allowed):  map[(y * 2) + 1 + offsets[1]][x * 2 + offsets[0]] = CellTypes.PATH.value
            if (right_allowed): map[y * 2 + offsets[0]][(x * 2) + 1 + offsets[0]] = CellTypes.PATH.value
            if (left_allowed):  map[y * 2 + offsets[0]][(x * 2) - 1 + offsets[0]] = CellTypes.PATH.value

            # NOTE: Vertices
            map[y * 2 + offsets[1]][x * 2 + offsets[0]] = CellTypes.PATH.value

        return map

    def update_render_cell(self, coordinates):
        (i, j) = coordinates

        grid_width = len(self.maze_map)

        if self.maze_map[j][i] == CellTypes.PATH.value:
            current_color = CellColors.BACKGROUND
        elif self.maze_map[j][i] == CellTypes.WALL.value:
            current_color = CellColors.WALL
        elif self.maze_map[j][i] == CellTypes.PLAYER.value:
            current_color = CellColors.PLAYER
        elif self.maze_map[j][i] == CellTypes.AI.value:
            current_color = CellColors.AI
        elif self.maze_map[j][i] == CellTypes.PLAYER_AND_AI.value:
            current_color = CellColors.PLAYER_AND_AI

        cell_size = (Global.BOARD_SIZE[0] // grid_width, Global.BOARD_SIZE[1] // grid_width)
        cell_position = (i * cell_size[0], j * cell_size[1])

        # 2D to 1D
        index = i * grid_width + j

        self.render_data[index] = (current_color, cell_size, cell_position)

    def update_cell(self, coordinates, value):
        (i, j) = coordinates
        self.maze_map[j][i] = value
        self.update_render_cell((i, j))

    def get_render_data(self):
        return self.render_data

    def initialize_render_data(self):
        grid_width = len(self.maze_map)

        for j in range(0, grid_width):
            for i in range(0, grid_width):
                self.update_render_cell((i, j))
