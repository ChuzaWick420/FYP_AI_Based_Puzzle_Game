class CellTypes:
    INVALID        = {"value": -1, "color": (-1, -1, -1)}
    WALL           = {"value": 0, "color": (255, 255, 255)} # WARN: A star algo probably makes assumption that WALL = 0
    PATH           = {"value": 1, "color": (0, 0, 0)}       # WARN: A star algo probably makes assumption that PATH = 1
    PLAYER         = {"value": 2, "color": (16, 230, 30)}
    AI             = {"value": 3, "color": (214, 34, 21)}
    PLAYER_AND_AI  = {"value": 4, "color": (189, 159, 13)}
    BLINDER        = {"value": 5, "color": (179, 18, 50)}
    SOURCE         = {"value": 6, "color": (120, 250, 146)}
    GOAL           = {"value": 7, "color": (10, 57, 138)}
    POWERUP_REVEAL = {"value": 8, "color": (116, 7, 138)}
    POWERUP_SLOW   = {"value": 9, "color": (255, 120, 3)}
