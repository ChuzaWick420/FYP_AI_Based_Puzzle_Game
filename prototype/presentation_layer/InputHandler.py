from prototype.Data_Layer.SystemEvents import SystemEvents
import pygame

class InputHandler:
    def __init__(self):
        self.system_events = []
        self.controls_map = {
            "UP": pygame.K_w,
            "DOWN": pygame.K_s,
            "LEFT": pygame.K_a,
            "RIGHT": pygame.K_d,
        }
        return

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.system_events.append(SystemEvents.TERMINATE_GAME)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.system_events.append(SystemEvents.MOUSE_CLICK)

            if event.type == pygame.KEYDOWN:
                if event.key == self.controls_map["UP"]:
                    self.system_events.append(SystemEvents.UP_PRESSED)
                if event.key == self.controls_map["DOWN"]:
                    self.system_events.append(SystemEvents.DOWN_PRESSED)
                if event.key == self.controls_map["LEFT"]:
                    self.system_events.append(SystemEvents.LEFT_PRESSED)
                if event.key == self.controls_map["RIGHT"]:
                    self.system_events.append(SystemEvents.RIGHT_PRESSED)

            if event.type == pygame.KEYUP:
                self.system_events.append(SystemEvents.KEY_RELEASE)

        return self.system_events

    def reset(self):
        self.system_events = []

    def createEvent(self, event):
        self.system_events.append(event)
