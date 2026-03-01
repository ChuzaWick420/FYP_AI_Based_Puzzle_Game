from prototype.Data_Layer.SystemEvents import SystemEvents
import pygame

class InputHandler:
    def __init__(self):
        self.system_events = []
        return

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.system_events.append(SystemEvents.TERMINATE_GAME)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.system_events.append(SystemEvents.MOUSE_CLICK)

        return self.system_events

    def reset(self):
        self.system_events = []

    def createEvent(self, event):
        self.system_events.append(event)
