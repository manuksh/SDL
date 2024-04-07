"""A listener is a software component or module that is designed to listen for and respond to 
specific events or signals within a system or application. It essentially acts as an event handler, 
waiting for certain events to occur and then executing predefined actions or processes in response.

Listeners are commonly used in various software architectures and systems, including graphical user 
interfaces (GUIs), web applications, network services, and more. They help decouple different parts 
of a system by allowing components to communicate indirectly through events rather than directly invoking 
each other's methods or functions.

In the context of a Descriptor, a Listener component might be described in its descriptor with details 
about the types of events it listens for, the sources or triggers of those events, and the actions it 
performs in response to them. This information helps developers understand the role and behavior of the 
Listener within the system.

{
    "Type": "Descriptor_Listener",
    "Event_Type": "User Interaction",
    "Source": "GUI Interface",
    "Target": "Application Logic"
}

In this example:
Type: Indicates that this descriptor is for a Listener component.
Event_Type: Describes the type of event that the Listener is designed to handle, such as "User Interaction", 
"Data Input", etc.
Source: Specifies the source or origin of the events that the Listener listens for. In this case, it's a 
"GUI Interface", indicating that the events come from a graphical user interface.
Target: Indicates the component or module within the system that responds to the events captured by the 
Listener. In this example, it's the "Application Logic", suggesting that the events trigger actions or 
processes within the application's logic layer.
"""


import json

class Descriptor_Listener:
    def __init__(self, name, decription, event_type, source, target):
        self.type = 'Descriptor_Listener'
        self.name = name,
        self.descrition = decription,
        self.event_type = event_type
        self.source = source
        self.target = target

    def get_descriptor_dict(self):
        return {
            'Type': self.type,
            'Name': self.name,
            'Event_Type': self.event_type,
            'Source': self.source,
            'Target': self.target
        }

    def get_descriptor(self):
        return json.dumps(self.get_descriptor_dict(), indent=4)


def test():
    # Example usage:
    listener_descriptor = Descriptor_Listener(
        name="Example Listener",
        decription="Description of the example listener.",
        event_type="User Interaction",
        source="GUI Interface",
        target="Application Logic"
    )
    print(listener_descriptor.get_descriptor())


if __name__ == "__main__":
    test()