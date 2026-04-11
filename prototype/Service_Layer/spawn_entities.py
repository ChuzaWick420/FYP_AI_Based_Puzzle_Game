from prototype.Data_Layer.CellTypes import CellTypes


def spawn_entities(grid):

    # TODO: Spawn power ups

    # grid_width = len(grid)
    # for j in range(0, grid_width):
    #     for i in range(0, grid_width):
    #         if grid[j][i] == CellTypes.PATH:
    #

    grid[1][0] = CellTypes.PLAYER_AND_AI.value
