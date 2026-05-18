from src.Data_Layer.ButtonType import ButtonType
from src.Data_Layer.StateInputs import StateInputs
from src.Presentation_Layer.TextElement import TextElement
from src.Presentation_Layer.menus.Menu import Menu
from src.Data_Layer import Global
from src.Presentation_Layer.Button import Button

class ScoreBoardMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        self.text.setText("Score Board Menu")
        self.text.setPosition(Global.MENU_TITLE_POS)

        self.buttons.append(Button("Home", StateInputs.EXIT, (80, 80)))

        self.buttons[0].loadIcon("assets/home_button.png")

        for button in self.buttons:
            button.setType(ButtonType.VISUAL)

        self.scores = []
        color = (176, 228, 204)

        pos = Global.MENU_TITLE_POS
        gap = 50

        for i in range(1, 6):
            (x, y) = (pos[0], pos[1] + i * gap)
            self.scores.append(TextElement("Temp", color, (x, y)))

        self.num_of_wins = TextElement("Wins: 0", color, (pos[0], pos[1] + 6 * gap))
        self.num_of_loses = TextElement("Loses: 0", color, (pos[0], pos[1] + 7 * gap))

    def render(self, display):

        self.text.render(display)
        self.num_of_wins.render(display)
        self.num_of_loses.render(display)

        for button in self.buttons:
            button.render(display)

        for score in self.scores:
            score.render(display)

    def setWins(self, wins):
        self.num_of_wins.setText(f"Wins: {wins}")

    def setLoses(self, loses):
        self.num_of_loses.setText(f"Loses: {loses}")

    def setScores(self, scores_data):
        for index in range(len(self.scores)):
            self.scores[index].setText(scores_data[index])
