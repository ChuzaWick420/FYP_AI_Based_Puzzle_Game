from prototype.entities.Graph import Graph
from prototype.entities.maze_type import MazeType
from prototype.entities.type_to_size_map import Type_Size_Map

def level_to_graph(level):
    type_value = (level - 1) % 3 + 1

    maze = MazeType(type_value)

    size = Type_Size_Map[maze.name]

    return Graph(size)
