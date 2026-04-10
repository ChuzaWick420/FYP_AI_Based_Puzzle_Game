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
                get_random_int(1, width - 2),
                get_random_int(1, width - 2)
            )

        # TODO: Calculate offsets
        cell_size = 16

        offsets = (
            (Global.WINDOW_RESOLUTION[0] - 16 * width) // 2,
            (Global.WINDOW_RESOLUTION[1] - 16 * width) // 2
        )

        print("Grid Width: ", width)
        print("In grid : ", pos)

        # new_pos = (pos[0] * cell_size + offsets[0], pos[1] * cell_size + offsets[1])

        # new_pos = (
        #     Global.WINDOW_RESOLUTION[0] // 2,
        #     Global.WINDOW_RESOLUTION[1] // 2
        # )

        new_pos = (54, 60)

        print("In screen : ", new_pos)

        self.updatePosition(new_pos)
        # self.updatePosition(pos)

