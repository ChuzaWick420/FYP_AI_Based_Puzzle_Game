import math
import random
from src.Data_Layer import Global
from src.Data_Layer.CellTypes import CellTypes
from src.Domain_Logic_Layer.algorithms.a_star_search_algo import a_star_search
from src.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from src.Domain_Logic_Layer.entities.Blinder import Blinder
from src.Domain_Logic_Layer.entities.Graph import Graph
from src.Domain_Logic_Layer.entities.PowerUp import PowerUp


class MapsManager:
    def __init__(self):
        self.__frame_buffer = []
        self.__blinders = []
        self.__level_num = -1

    def createGraph(self, level_number, saved_mst = None):
        self.__level_num = level_number
        size = (level_number * 3) ** 2
        self.__graph = Graph(size)

        # NOTE: If there was no previous graph provided, use prim's algorithm to generate one
        if (saved_mst == None):
            mst = prims_algorithm(self.__graph)
            self.__graph.setAdjMatrix(mst)
        else:
            self.__graph.setAdjMatrix(saved_mst)

    def initialize(self):

        self.__maze_map = self.__generate_grid_map()
        map_width = len(self.__maze_map)
        self.__blinders_map = [[CellTypes.INVALID["value"]] * map_width for _ in range(map_width)]
        self.__entities_map = [[CellTypes.INVALID["value"]] * map_width for _ in range(map_width)]
        self.__specials_map = [[CellTypes.INVALID["value"]] * map_width for _ in range(map_width)]

        self.__frame_buffer = [((-1, -1, -1), (-1, -1), (-1, -1))] * (map_width ** 2)
        self.__search()
        self.spawn_powerups()
        self.__initializeFrameBuffer()

    def __search(self):

        size = len(self.__maze_map)

        # NOTE: Format: (y, x)
        src = [1, 0]
        dest = [size - 2, size - 1]

        # NOTE: Get the path before populating the grid
        self.path = a_star_search(self.__maze_map, src, dest, size)

    def __popBlinder(self):
        self.__blinders.pop()

        # NOTE: Refresh blinder's map
        map_width = len(self.__maze_map)

        self.__blinders_map = [[CellTypes.INVALID["value"]] * map_width for _ in range(map_width)]
        self.__injectBlinders()

    def __injectBlinders(self):
        for blinder in self.__blinders:
            pos = blinder.getPosition()
            size = blinder.getSize()

            # FIXME: This section is ran sometimes when 
            #        reveal powerup is taken and blinders have not spawned
            print(f"DEBUGGING - position: {pos}")
            print(f"DEBUGGING - size: {size}")
            print(f"DEBUGGING - map: {self.__blinders_map}")

            for j in range(pos[1], pos[1] + size):
                for i in range(pos[0], pos[0] + size):
                    self.__blinders_map[j][i] = CellTypes.BLINDER["value"]

        # NOTE: Update render cells for whole maze
        self.__initializeFrameBuffer()

    def spawn_blinders(self):
        maze_width = len(self.__maze_map)
        self.__blinders = []

        for _ in range(self.__level_num * 2):
            blinder = Blinder()

            # NOTE: Level number to size
            blinder.setSize(int(math.sqrt(maze_width)))

            blinder_size = blinder.getSize()

            x = random.randint(0, maze_width - blinder_size)
            y = random.randint(0, maze_width - blinder_size)

            blinder.setPosition((x, y))
            self.__blinders.append(blinder)

        self.__injectBlinders()

    def spawn_powerups(self):
        maze_width = len(self.__maze_map)
        powerups = []

        i = 0

        while (i < self.__level_num):
            powerup = PowerUp()

            x = random.randint(1, maze_width - 1)
            y = random.randint(1, maze_width - 1)

            if (self.__maze_map[y][x] != CellTypes.WALL["value"]):
                powerup.setPosition((x, y))

                powerup_type = random.randint(
                    CellTypes.POWERUP_REVEAL["value"],
                    CellTypes.POWERUP_SLOW["value"]
                )

                powerup.setType(powerup_type)
                powerups.append(powerup)

                i += 1

        for powerup in powerups:
            (x, y) = powerup.getPosition()
            powerup_type = powerup.getType()
            self.__specials_map[y][x] = powerup_type

        self.__initializeFrameBuffer()

    def disable_random_blinders(self):

        amount_to_disable = 0

        if len(self.__blinders) > 0:
            amount_to_disable = random.randint(1, len(self.__blinders))

        for _ in range(amount_to_disable):
            self.__popBlinder()

    def __generate_grid_map(self):
        # NOTE: Nodes + Edges
        nodes_amount_1D = self.__graph.getWidth()
        edges_amount_1D = nodes_amount_1D - 1
        padding = 1 + 1
        grid_width = nodes_amount_1D + edges_amount_1D + padding

        map = [[0] * grid_width for _ in range(grid_width)]

        # NOTE: Goes through padding (up and down)
        for i in range(0, grid_width):
            map[0][i] = CellTypes.WALL["value"]
            map[grid_width - 1][i] = CellTypes.WALL["value"]

        # NOTE: Goes through padding (right and left)
        for i in range(0, grid_width):
            map[i][0] = CellTypes.WALL["value"]
            map[i][grid_width - 1] = CellTypes.WALL["value"]

        # NOTE: Create openings within padding
        map[1][0] = CellTypes.PATH["value"]
        map[grid_width - 2][grid_width - 1] = CellTypes.PATH["value"]

        offsets = (1, 1)

        nodes_count = self.__graph.getNodesCount()
        matrix = self.__graph.getAdjMatrix()
        graph_width = self.__graph.getWidth()

        # NOTE: Goes through each vertex
        for node_index in range(0, nodes_count):

            (x, y) = self.__graph.index_to_coordinates(node_index)

            up_allowed    = y - 1 >= 0          and matrix[node_index][self.__graph.coordinates_to_index(x, y - 1)] != 0
            down_allowed  = y + 1 < graph_width and matrix[node_index][self.__graph.coordinates_to_index(x, y + 1)] != 0
            right_allowed = x + 1 < graph_width and matrix[node_index][self.__graph.coordinates_to_index(x + 1, y)] != 0
            left_allowed  = x - 1 >= 0          and matrix[node_index][self.__graph.coordinates_to_index(x - 1, y)] != 0

            if (up_allowed):    map[(y * 2) - 1 + offsets[1]][x * 2 + offsets[0]] = CellTypes.PATH["value"]
            if (down_allowed):  map[(y * 2) + 1 + offsets[1]][x * 2 + offsets[0]] = CellTypes.PATH["value"]
            if (right_allowed): map[y * 2 + offsets[0]][(x * 2) + 1 + offsets[0]] = CellTypes.PATH["value"]
            if (left_allowed):  map[y * 2 + offsets[0]][(x * 2) - 1 + offsets[0]] = CellTypes.PATH["value"]

            # NOTE: Vertices
            map[y * 2 + offsets[1]][x * 2 + offsets[0]] = CellTypes.PATH["value"]

        return map

    def updateFrameCell(self, coordinates):
        (i, j) = coordinates

        grid_width = len(self.__maze_map)

        current_color = (-1, -1, -1)

        # NOTE: Layering (top to bottom)
        # 1. Entities
        # 2. Others
        # 3. Blinders
        # 4. Maze

        # NOTE: Entities
        if self.__entities_map[j][i] == CellTypes.AI["value"]:
            current_color = CellTypes.AI["color"]
        elif self.__entities_map[j][i] == CellTypes.PLAYER["value"]:
            current_color = CellTypes.PLAYER["color"]
        elif self.__entities_map[j][i] == CellTypes.PLAYER_AND_AI["value"]:
            current_color = CellTypes.PLAYER_AND_AI["color"]
        elif self.__entities_map[j][i] == CellTypes.INVALID["value"]:
            # NOTE: Others
            if self.__specials_map[j][i] == CellTypes.POWERUP_SLOW["value"]:
                current_color = CellTypes.POWERUP_SLOW["color"]
            elif self.__specials_map[j][i] == CellTypes.POWERUP_REVEAL["value"]:
                current_color = CellTypes.POWERUP_REVEAL["color"]
            elif self.__specials_map[j][i] == CellTypes.SOURCE["value"]:
                current_color = CellTypes.SOURCE["color"]
            elif self.__specials_map[j][i] == CellTypes.GOAL["value"]:
                current_color = CellTypes.GOAL["color"]
            elif self.__specials_map[j][i] == CellTypes.INVALID["value"]:
                # NOTE: Blinders
                if self.__blinders_map[j][i] == CellTypes.BLINDER["value"]:
                    current_color = CellTypes.BLINDER["color"]
                elif self.__blinders_map[j][i] == CellTypes.INVALID["value"]:
                    # NOTE: Maze
                    if self.__maze_map[j][i] == CellTypes.PATH["value"]:
                        current_color = CellTypes.PATH["color"]
                    elif self.__maze_map[j][i] == CellTypes.WALL["value"]:
                        current_color = CellTypes.WALL["color"]

        cell_size = (Global.BOARD_SIZE[0] // grid_width, Global.BOARD_SIZE[1] // grid_width)
        cell_position = (i * cell_size[0], j * cell_size[1])

        # 2D to 1D
        index = i * grid_width + j

        self.__frame_buffer[index] = (current_color, cell_size, cell_position)

    def setEntitiesCell(self, coordinates, value):
        (i, j) = coordinates
        self.__entities_map[j][i] = value
        self.updateFrameCell((i, j))

    def getFrameBuffer(self):
        return self.__frame_buffer

    def __initializeFrameBuffer(self):
        grid_width = len(self.__maze_map)

        src = (0, 1)
        goal = (grid_width - 1, grid_width - 2)

        self.__specials_map[src[1]][src[0]] = CellTypes.SOURCE["value"]
        self.__specials_map[goal[1]][goal[0]] = CellTypes.GOAL["value"]

        for j in range(0, grid_width):
            for i in range(0, grid_width):
                self.updateFrameCell((i, j))

    def getMST(self):
        return self.__graph.getAdjMatrix()

    def getSpecialsMap(self):
        return self.__specials_map

    def getBlindersMap(self):
        return self.__blinders_map

    def getEntitiesMap(self):
        return self.__entities_map

    def getMazeMap(self):
        return self.__maze_map

    def setSpecialCell(self, pos, cell_value):
        self.__specials_map[pos[1]][pos[0]] = cell_value
