from prototype.entities.Graph import Graph
from prototype.entities.maze_type import MazeType

def level_to_size(level):
    type_of_maze = (level - 1) % 3 + 1

    map = {
        "SMALL": 3 * 3,
        "MEDIUM": 9 * 9,
        "LARGE": 12 * 12,
    }

    return Graph(
        map[MazeType(type_of_maze).name]
    )
