from prototype.Presentation_Layer.Visual_entity import VisualEntity


class Ai(VisualEntity):
    def __init__(self):
        super().__init__()
        color = (214, 34, 21)
        self.updateColor(color)
