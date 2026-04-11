from enum import Enum

class CellTypes(Enum):
    WALL = 0
    PATH = 1
    PLAYER = 2
    AI = 3
    PLAYER_AND_AI = 4
