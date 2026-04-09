from prototype.Presentation_Layer.Visual_entity import VisualEntity


class Player(VisualEntity):
    def __init__(self):
        super().__init__()
        color = (16, 230, 30)
        self.updateColor(color)
