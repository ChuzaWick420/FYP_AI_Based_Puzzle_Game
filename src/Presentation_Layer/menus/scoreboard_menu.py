from src.Data_Layer.ButtonType import ButtonType
from src.Data_Layer.StateInputs import StateInputs
from src.Presentation_Layer.TextElement import TextElement
from src.Presentation_Layer.menus.Menu import Menu
from src.Data_Layer import Global
from src.Presentation_Layer.Button import Button

class ScoreBoardMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        starting_offset = 200
        gap = 50

        pos = (Global.WINDOW_RESOLUTION[0] // 2, starting_offset)

        self.text.setText("Score Board Menu")
        self.text.setPosition((pos[0], pos[1] - 2 * gap))

        self.buttons.append(Button("Home", StateInputs.EXIT, (80, 80)))

        self.buttons[0].loadIcon("assets/home_button.png")

        for button in self.buttons:
            button.setType(ButtonType.VISUAL)

        self.scores = []
        temp_color = (232, 93, 7)

        self.num_of_wins = TextElement("Wins: 0", temp_color, (pos[0], pos[1] + 6 * gap))
        self.num_of_loses = TextElement("Loses: 0", temp_color, (pos[0], pos[1] + 7 * gap))

        for i in range(5):
            (x, y) = (pos[0], pos[1] + i * gap)
            self.scores.append(TextElement("Temp", temp_color, (x, y)))

    def render(self, display):

        display.blit(self.text.text, self.text.textRect)
        display.blit(self.num_of_wins.text, self.num_of_wins.textRect)
        display.blit(self.num_of_loses.text, self.num_of_loses.textRect)

        for button in self.buttons:
            button.render(display)

        for score in self.scores:
            display.blit(score.text, score.textRect)
