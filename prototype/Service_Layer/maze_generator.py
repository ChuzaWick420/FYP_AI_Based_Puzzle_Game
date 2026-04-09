import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, color, dimensions, position):
        super().__init__()

        width = dimensions[0]
        height = dimensions[1]

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = position[0] * width
        self.rect.y = position[1] * height

def generate_maze(grid):
    maze_visual = pygame.sprite.Group()

    background_color = (0, 0, 0)
    wall_color = (255, 255, 255)
    current_color    = (0, 0, 0)

    grid_width = len(grid)

    for j in range(0, grid_width):
        for i in range(0, grid_width):
            if grid[j][i] == 1:
                current_color = background_color
            else:
                current_color = wall_color

            maze_visual.add(Block(current_color, (16, 16), (i, j)))

    return maze_visual
