from prototype.entities.Button import Button
from prototype.entities.TextElement import TextElement
from prototype.menus.Menu import Menu
from prototype.data import Global

class ResultMenu(Menu):
    def __init__(self):
        Menu.__init__(self)

        starting_offset = 200
        gap = 50

        pos = (Global.WINDOW_RESOLUTION[0] // 2, starting_offset)

        self.text.updateText("Result Menu")
        self.text.setPosition((pos[0], pos[1] - 3 * gap))

        # Extras
        color = (254, 197, 43)
        self.winner_info = TextElement("You Win!", color, (pos[0], pos[1] - 2 * gap))
        self.completion_time = TextElement("Timer:", color, (pos[0], pos[1] - 1 * gap))

        self.buttons.append(Button("Restart Level", (pos[0], pos[1] + 0 * gap)))
        self.buttons.append(Button("Scoreboard", (pos[0], pos[1] + 1 * gap)))
        self.buttons.append(Button("Home",       (pos[0], pos[1] + 2 * gap)))

    def render(self, display):
        display.blit(self.text.text, self.text.textRect)
        display.blit(self.winner_info.text, self.winner_info.textRect)
        display.blit(self.completion_time.text, self.completion_time.textRect)

        for button in self.buttons:
            button.render(display)

    def setTimer(self, time):
        self.completion_time.updateText(time)
