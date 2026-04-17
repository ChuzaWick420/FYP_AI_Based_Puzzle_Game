import pygame

class Border:
    def __init__(self, reference_rect):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.width = 250
        self.padding = 16
        self.color = (255, 255, 255)
        self.thickness = 2
        self.border_radius = 8

        self.rect.width = self.width
        self.rect.height = reference_rect.height + self.padding
        self.rect.center = reference_rect.center

    def render(self, display):
        pygame.draw.rect(display, self.color, self.rect, self.thickness, self.border_radius)
