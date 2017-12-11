from listener import Listener


class EventManager:
    def __init__(self):
        self.event_to_handler_map = {}

    def add_event(self, eventName):
        if eventName in self.event_to_handler_map:
            print("ERROR (add_event): Event {event} already exists!".format(event=eventName))
        else:
            self.event_to_handler_map[eventName] = {}

    def remove_event(self, eventName):
        if eventName not in self.event_to_handler_map:
            print("ERROR (remove_event): Event {event} does not exist!".format(event=eventName))
        else:
            del self.event_to_handler_map[eventName]

    def add_listener_to_event(self, eventName, listenerName, listenerObject):
        if eventName not in self.event_to_handler_map:
            print("ERROR (add_listener_to_event): Could not find event {event}!".format(event=eventName))
        elif listenerName in self.event_to_handler_map[eventName]:
            print("ERROR (add_listener_to_event): Listener {listener} already exists!".format(listener=listenerName))
        else:
            self.event_to_handler_map[eventName][listenerName] = listenerObject

    def remove_listener_from_event(self, eventName, listenerName):
        if eventName not in self.event_to_handler_map:
            print("ERROR (remove_listener_from_event): Could not find event {event}!".format(event=eventName))
        elif listenerName not in self.event_to_handler_map[eventName]:
            print("ERROR (remove_listener_from_event): Could not find listener {listener}!".format(listener=listenerName))
        else:
            del self.event_to_handler_map[eventName][listenerName]

    def trigger_event(self, eventName):
        if eventName not in self.event_to_handler_map:
            print("ERROR (trigger_event): Could not find event {event}!".format(event=eventName))
        else:
            for listenerName, listenerObject in self.event_to_handler_map[eventName].items():
                listenerObject.catch_event(eventName)


if __name__ == '__main__':
    em = EventManager()

    em.add_event("Event A")
    em.add_event("Event B")
    em.add_event("Event C")

    em.add_listener_to_event("Event A", "Listener X", Listener("Listener X"))
    em.add_listener_to_event("Event A", "Listener Y", Listener("Listener Y"))
    em.add_listener_to_event("Event A", "Listener Z", Listener("Listener Z"))

    em.add_listener_to_event("Event B", "Listener P", Listener("Listener P"))
    em.add_listener_to_event("Event B", "Listener U", Listener("Listener U"))
    em.add_listener_to_event("Event B", "Listener K", Listener("Listener K"))

    em.trigger_event("Event A")