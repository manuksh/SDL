



#######################################################
## Descriptor_Event
class Descriptor_Event():
    def __init__(self, name, description, event_type, source, target, data):
        self.type = "Descriptor_Event"
        self.name = name
        self.description = description
        self.event_type = event_type
        self.source = source
        self.target = target
        self.data  = data

    def get_descriptor_dict(self):
            return {
                "Type": self.type,
                "Name": self.name,
                "Description": self.description,
                "Event_Type": self.event_type,
                "Source": self.source,
                "Target": self.target
            }

    def get_descriptor(self):
        return json.dumps(self.get_descriptor_dict(), indent=4)
    

def test():
    # Example usage:
    event_descriptor = Descriptor_Event(
        name="Example Event",
        description="Description of the example event.",
        event_type="User Interaction",
        source="GUI Interface",
        target="Application Logic",
        data = {
            "Input_Data": "The data to be processed.",
            "Options": "Optional parameters for customizing the processing."
        }
    )
    print(event_descriptor.get_descriptor())

    if __name__ == "__main__":
        test()  