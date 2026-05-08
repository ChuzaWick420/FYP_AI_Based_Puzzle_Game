from src.Data_Layer import Global
from src.Data_Layer.ButtonType import ButtonType
from src.Data_Layer.StateInputs import StateInputs
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
        self.buttons.append(Button("Play",              StateInputs.PLAY,                 (pos[0], pos[1] + 0 * gap)))
        self.buttons.append(Button("Select Difficulty", StateInputs.DIFFICULTY_SELECTION, (pos[0], pos[1] + 1 * gap)))
        self.buttons.append(Button("Scoreboard",        StateInputs.SCORE_BOARD,          (pos[0], pos[1] + 2 * gap)))
        self.buttons.append(Button("Quit",              StateInputs.EXIT,                 (pos[0], pos[1] + 3 * gap)))

        for button in self.buttons:
            button.setType(ButtonType.TEXTUAL)
