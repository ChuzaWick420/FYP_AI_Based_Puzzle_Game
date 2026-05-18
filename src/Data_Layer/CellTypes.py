from src.Data_Layer.Colors import Colors


class CellTypes:
    INVALID        = {"value": -1, "color": (-1, -1, -1)}
    WALL           = {"value": 0, "color": Colors.WALL} # WARN: A star algo probably makes assumption that WALL = 0
    PATH           = {"value": 1, "color": Colors.PATH}       # WARN: A star algo probably makes assumption that PATH = 1
    PLAYER         = {"value": 2, "color": Colors.PLAYER}
    AI             = {"value": 3, "color": Colors.AI}
    PLAYER_AND_AI  = {"value": 4, "color": Colors.PLAYER_AND_AI}
    # BLINDER        = {"value": 5, "color": (179, 18, 50)} # NOTE: Turn these on for debugging
    BLINDER        = {"value": 5, "color": Colors.BLINDER}
    SOURCE         = {"value": 6, "color": Colors.SOURCE}
    GOAL           = {"value": 7, "color": Colors.GOAL}
    POWERUP_REVEAL = {"value": 8, "color": Colors.POWERUP_REVEAL}
    POWERUP_SLOW   = {"value": 9, "color": Colors.POWERUP_SLOW}
