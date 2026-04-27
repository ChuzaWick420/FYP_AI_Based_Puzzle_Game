from src.Data_Layer import Global
from src.Data_Layer.ButtonType import ButtonType
from src.Presentation_Layer.Button import Button
from src.Presentation_Layer.menus.Menu import Menu

class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        starting_offset = 200
        gap = 50

        pos = (Global.WINDOW_RESOLUTION[0] // 2, starting_offset)

        self.text.setText("Memory Maze - Human vs AI Pathfinding Game")

        self.text.setPosition((pos[0], pos[1] - 2 * gap))

        # Buttons
        self.buttons.append(Button("Play",              (pos[0], pos[1] + 0 * gap)))
        self.buttons.append(Button("Select Difficulty", (pos[0], pos[1] + 1 * gap)))
        self.buttons.append(Button("Scoreboard",       (pos[0], pos[1] + 2 * gap)))
        self.buttons.append(Button("Quit",              (pos[0], pos[1] + 3 * gap)))

        for button in self.buttons:
            button.setType(ButtonType.TEXTUAL)
