class GenericListener:
    def __init__(self, listenerName):
        self.listenerName = listenerName

    def catch_event(self, eventName):
        print("{listener}: Event {event} caught!!!".format(event=eventName, listener=self.listenerName))