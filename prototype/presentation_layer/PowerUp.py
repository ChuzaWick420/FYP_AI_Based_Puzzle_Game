from prototype.Presentation_Layer.Visual_entity import VisualEntity


class PowerUp(VisualEntity):
    def __init__(self):
        super().__init__()
        color = (30, 205, 214)
        self.updateColor(color)
