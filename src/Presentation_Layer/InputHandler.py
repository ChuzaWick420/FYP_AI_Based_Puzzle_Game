from src.Data_Layer.SystemEvents import SystemEvents
import pygame

class InputHandler:
    def __init__(self):
        self.controls_map = {
            "UP": pygame.K_UP,
            "DOWN": pygame.K_DOWN,
            "LEFT": pygame.K_LEFT,
            "RIGHT": pygame.K_RIGHT,
        }

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return SystemEvents.TERMINATE_GAME

            if event.type == pygame.MOUSEBUTTONDOWN:
                return SystemEvents.MOUSE_CLICK

            if event.type == pygame.KEYDOWN:
                if event.key == self.controls_map["UP"]:
                    return SystemEvents.UP_PRESSED
                if event.key == self.controls_map["DOWN"]:
                    return SystemEvents.DOWN_PRESSED
                if event.key == self.controls_map["LEFT"]:
                    return SystemEvents.LEFT_PRESSED
                if event.key == self.controls_map["RIGHT"]:
                    return SystemEvents.RIGHT_PRESSED
                if event.key == pygame.K_RETURN:
                    return SystemEvents.RETURN_PRESSED
                if event.key == pygame.K_ESCAPE:
                    return SystemEvents.PAUSE_PRESSED
                if event.key == pygame.K_p:
                    return SystemEvents.PAUSE_PRESSED

            if event.type == pygame.KEYUP:
                return SystemEvents.KEY_RELEASE

        return None
