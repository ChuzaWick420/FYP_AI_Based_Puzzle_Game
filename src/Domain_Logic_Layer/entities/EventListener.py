class EventListener:
    def __init__(self):
        self.events = []

    def createEvent(self, event):
        self.events.append(event)

    def getEvents(self):
        return self.events

    def reset(self):
        self.events = []
