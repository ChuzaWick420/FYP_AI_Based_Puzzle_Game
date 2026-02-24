import pygame

# Global
SCREEN_RESOLUTION = (800, 600)

pygame.init()

class Button:
    def __init__(self, button_name, pos):
        self.id = button_name
        color = (255, 100, 100)
        font = pygame.font.Font(None, 32)
        self.text = font.render(button_name, True, color)
        self.textRect = self.text.get_rect()
        self.textRect.center = pos
        self.position = pos

    def isClicked(self):
        flag = False

        mouse_pos = pygame.mouse.get_pos()

        horizontal_left  = mouse_pos[0] >= self.position[0] - self.textRect.width // 2
        horizontal_right = mouse_pos[0] <= self.position[0] + self.textRect.width // 2
        vertical_up      = mouse_pos[1] >= self.position[1] - self.textRect.height // 2
        vertical_down    = mouse_pos[1] <= self.position[1] + self.textRect.height // 2

        if (horizontal_left and horizontal_right and vertical_up and vertical_down):
            # TODO: REMOVE THIS DEBUG LATER ON
            print("Button Clicked") #debug
            flag = True

        return flag

class Menu:
    def __init__(self, resolution):
        self.foreground_color = (255, 100, 100)
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render('Hello World', True, self.foreground_color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (resolution[0] // 2, resolution[1] // 2)

        # Button
        self.test_button = Button("Play", (200, 400))
        self.another_button = Button("Quit", (200, 500))

        self.buttons = [
            self.test_button,
            self.another_button
        ]

    def render(self, screen_obj):
        screen_obj.blit(self.text, self.textRect)

        for button in self.buttons:
            screen_obj.blit(button.text, button.textRect)

class SystemEvents:
    # NOTE: Code Format xxff
    #       xx = 10 - Input Events
    #       xx = 11 - Window Events

    BUTTON_CLICK   = 1001
    TERMINATE_GAME = 1101

class InputHandler:
    def __init__(self):
        return

    def processEvents(self):
        events = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                events.append(SystemEvents.TERMINATE_GAME)

            if event.type == pygame.MOUSEBUTTONDOWN:
                events.append(SystemEvents.BUTTON_CLICK)

        return events

class Engine:
    def __init__(self, res):
        self.resolution = res
        self.test_menu = Menu(SCREEN_RESOLUTION)
        self.input_handler = InputHandler()

    def start(self):
        screen = pygame.display.set_mode(self.resolution)

        isRunning = True

        while isRunning:
            events = self.input_handler.processEvents()

            for event in events:
                if event == SystemEvents.TERMINATE_GAME:
                    isRunning = False

                if event == SystemEvents.BUTTON_CLICK:
                    for button in self.test_menu.buttons:
                        button.isClicked()

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")

            # RENDER YOUR GAME HERE
            self.test_menu.render(screen)

            # flip() the display to put your work on screen
            pygame.display.flip()

        pygame.quit()

engine = Engine(SCREEN_RESOLUTION) # initialize
engine.start()
