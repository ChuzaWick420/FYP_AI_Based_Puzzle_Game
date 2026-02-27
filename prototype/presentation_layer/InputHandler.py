from prototype.data.SystemEvents import SystemEvents
import pygame

class InputHandler:
    def __init__(self):
        return

    def processEvents(self):
        system_events = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                system_events.append(SystemEvents.TERMINATE_GAME)

            if event.type == pygame.MOUSEBUTTONDOWN:
                system_events.append(SystemEvents.MOUSE_CLICK)

        return system_events
