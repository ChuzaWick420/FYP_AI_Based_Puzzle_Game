from prototype.Domain_Logic_Layer.entities.Graph import get_random_int
from prototype.Presentation_Layer.Block import Block
from prototype.Data_Layer import Global

class VisualEntity:
    def __init__(self, color = (0, 0, 0), size = (8, 8), pos = (0, 0)):
        self.color = color
        self.size = size
        self.pos = pos
        self.sprite = Block(self.color, self.size, self.pos)

    def render(self, display):
        display.blit(self.sprite.image, self.sprite.rect)

    def updateColor(self, color):
        self.color = color
        self.sprite = Block(self.color, self.size, self.pos)

    def updateSize(self, size):
        self.size = size
        self.sprite = Block(self.color, self.size, self.pos)

    def updatePosition(self, pos):
        self.pos = pos
        self.sprite = Block(self.color, self.size, self.pos)

    def spawn(self, grid):
        width = len(grid)

        pos = (0, 0)

        while grid[pos[1]][pos[0]] != 1:
            pos = (
                get_random_int(1, width - 1),
                get_random_int(1, width - 1)
            )

        self.updatePosition((pos[0] + 269, pos[1] + 36))

