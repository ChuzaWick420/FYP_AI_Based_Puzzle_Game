import pygame

from prototype.Data_Layer import Global
from prototype.Data_Layer.CellColors import CellColors
from prototype.Data_Layer.CellTypes import CellTypes
from prototype.Presentation_Layer.Block import Block

def center_maze(maze):
    rects = [sprite.rect for sprite in maze.sprites()]
    group_rect = rects[0].unionall(rects[1:])

    offset_x = (Global.WINDOW_RESOLUTION[0] // 2) - group_rect.centerx
    offset_y = (Global.WINDOW_RESOLUTION[1] // 2) - group_rect.centery

    for sprite in maze:
        sprite.rect.x += offset_x
        sprite.rect.y += offset_y

def visualize_grid(grid):
    maze_visual = pygame.sprite.Group()

    current_color = (0, 0, 0)

    grid_width = len(grid)


    for j in range(0, grid_width):
        for i in range(0, grid_width):
            if grid[j][i] == CellTypes.PATH.value:
                current_color = CellColors.BACKGROUND
            elif grid[j][i] == CellTypes.WALL.value:
                current_color = CellColors.WALL
            elif grid[j][i] == CellTypes.PLAYER.value:
                current_color = CellColors.PLAYER
            elif grid[j][i] == CellTypes.AI.value:
                current_color = CellColors.AI
            elif grid[j][i] == CellTypes.PLAYER_AND_AI.value:
                current_color = CellColors.PLAYER_AND_AI

            cell_size = (Global.BOARD_SIZE[0] // grid_width, Global.BOARD_SIZE[1] // grid_width)
            cell_position = (i * cell_size[0], j * cell_size[1])

            maze_visual.add(Block(current_color, cell_size, cell_position))

    # NOTE: Center the maze visual
    center_maze(maze_visual)

    return maze_visual
