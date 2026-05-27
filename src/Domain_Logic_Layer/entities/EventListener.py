class EventListener:
    def __init__(self):
        self.__events = []

    def createEvent(self, event):
        self.__events.append(event)

    def getEvents(self):
        return self.__events

    def reset(self):
        self.__events = []

    def processed(self, event):
        self.__events.remove(event)
