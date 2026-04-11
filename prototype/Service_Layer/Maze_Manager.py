from prototype.Data_Layer import Global
from prototype.Data_Layer.CellColors import CellColors
from prototype.Data_Layer.CellTypes import CellTypes
from prototype.Domain_Logic_Layer.algorithms.a_star_search_algo import a_star_search
from prototype.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from prototype.Domain_Logic_Layer.entities.Graph import Graph
from prototype.Domain_Logic_Layer.entities.Grid_Map import Grid_Map
from prototype.Service_Layer.spawn_entities import spawn_entities


class Maze_Manager:
    def __init__(self):
        self.graph = Graph(16 * 16)

        mst = prims_algorithm(self.graph)
        self.graph.adj_matrix = mst

        self.maze_map = Grid_Map(self.graph).get_map()

        size = len(self.maze_map)

        # NOTE: Format: (y, x)
        src = [1, 0]
        dest = [size - 2, size - 1]

        # NOTE: Get the path before populating the grid
        self.path = a_star_search(self.maze_map, src, dest, size)

        spawn_entities(self.maze_map)

        # DEBUG:
        # print("Source: ", src)
        # print("Destination: ", dest)
        #
        # for row in self.maze_map:
        #     print(row)

    def get_render_data(self):
        render_data = []
        current_color = (0, 0, 0)
        grid_width = len(self.maze_map)

        for j in range(0, grid_width):
            for i in range(0, grid_width):

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

                render_data.append((current_color, cell_size, cell_position))

        return render_data
