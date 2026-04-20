class CellTypes:
    WALL          = {"value": 0, "color": (255, 255, 255)} # WARN: A star algo probably makes assumption that WALL = 0
    PATH          = {"value": 1, "color": (0, 0, 0)}       # WARN: A star algo probably makes assumption that PATH = 1
    PLAYER        = {"value": 2, "color": (16, 230, 30)}
    AI            = {"value": 3, "color": (214, 34, 21)}
    PLAYER_AND_AI = {"value": 4, "color": (189, 159, 13)}
